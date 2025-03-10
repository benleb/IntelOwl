# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

from datetime import timedelta

from intezer_sdk import api as intezer_api, errors as intezer_errors
from intezer_sdk.analysis import Analysis

from api_app.exceptions import AnalyzerRunException
from api_app.analyzers_manager.classes import FileAnalyzer

from tests.mock_utils import patch, if_mock_connections


class IntezerScan(FileAnalyzer):
    def set_params(self, params):
        # soft time limit
        soft_time_limit = params.get("soft_time_limit", 300)
        self.timeout = soft_time_limit - 5
        # interval
        self.poll_interval = 3
        # disable_dynamic_unpacking
        self.disable_dynamic_unpacking = params.get("disable_dynamic_unpacking", False)
        # disable_static_unpacking
        self.disable_static_unpacking = params.get("disable_static_unpacking", False)
        # upload file or not
        self.upload_file = params.get("upload_file", True)
        intezer_api.set_global_api(api_key=self._secrets["api_key_name"])

    def run(self):
        result = {}

        try:
            # run analysis by hash
            hash_result = self.__intezer_analysis(file_hash=self.md5)
            result.update(hash_result, hash_found=True)
        except intezer_errors.HashDoesNotExistError as e:
            if not self.upload_file:
                raise AnalyzerRunException(e)
            # else, run analysis by file
            file_result = self.__intezer_analysis(file_stream=self.read_file_bytes())
            result.update(file_result, hash_found=False)
        except intezer_errors.IntezerError as e:
            raise AnalyzerRunException(e)

        return result

    def __intezer_analysis(self, **kwargs) -> dict:
        analysis = Analysis(
            **kwargs,
            disable_dynamic_unpacking=self.disable_dynamic_unpacking,
            disable_static_unpacking=self.disable_static_unpacking,
            file_name=self.filename,
        )
        analysis.send(wait=False)
        analysis.wait_for_completion(
            interval=self.poll_interval,
            sleep_before_first_check=True,
            timeout=timedelta(seconds=self.timeout),
        )
        return analysis.result()

    @classmethod
    def _monkeypatch(cls):
        patches = [
            if_mock_connections(
                patch.object(Analysis, "send", return_value=None),
                patch.object(Analysis, "wait_for_completion", return_value=None),
                patch.object(Analysis, "result", return_value={"test": "test"}),
            )
        ]
        return super()._monkeypatch(patches=patches)
