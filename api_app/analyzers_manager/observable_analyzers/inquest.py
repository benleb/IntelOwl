# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

import re
import logging
import requests

from api_app.exceptions import AnalyzerRunException, AnalyzerConfigurationException
from api_app.analyzers_manager.classes import ObservableAnalyzer

from tests.mock_utils import if_mock_connections, patch, MockResponse


logger = logging.getLogger(__name__)


class InQuest(ObservableAnalyzer):
    base_url: str = "https://labs.inquest.net"

    def set_params(self, params):
        self.__api_key = self._secrets["api_key_name"]
        self.analysis_type = params.get("inquest_analysis", "dfi_search")
        self.generic_identifier_mode = "user-defined"  # Or auto

    @property
    def hash_type(self):
        hash_lengths = {32: "md5", 40: "sha1", 64: "sha256", 128: "sha512"}
        hash_type = hash_lengths.get(len(self.observable_name), None)
        if not hash_type:
            raise AnalyzerRunException(
                f"Given Hash: '{hash}' is not suported."
                "Supported hash types are: 'md5', 'sha1', 'sha256', 'sha512'."
            )
        return hash_type

    def type_of_generic(self):
        if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", self.observable_name):
            type_ = "email"
        else:
            # TODO: This should be validated more thoroughly
            type_ = "filename"
        return type_

    def run(self):
        result = {}
        headers = {"Content-Type": "application/json"}
        if self.__api_key:
            headers["Authorization"] = self.__api_key
        else:
            warning = "No API key retrieved"
            logger.info(
                f"{warning}. Continuing without API key..." f" <- {self.__repr__()}"
            )
            self.report.errors.append(warning)

        if self.analysis_type == "dfi_search":
            if self.observable_classification == self.ObservableTypes.HASH:
                uri = (
                    f"/api/dfi/search/hash/{self.hash_type}?hash={self.observable_name}"
                )

            elif self.observable_classification in [
                self.ObservableTypes.IP,
                self.ObservableTypes.URL,
                self.ObservableTypes.DOMAIN,
            ]:
                uri = (
                    f"/api/dfi/search/ioc/{self.observable_classification}"
                    f"?keyword={self.observable_name}"
                )

            elif self.observable_classification == self.ObservableTypes.GENERIC:
                try:
                    type_, value = self.observable_name.split(":")
                except ValueError:
                    self.generic_identifier_mode = "auto"
                    type_ = self.type_of_generic()
                    value = self.observable_name

                if type_ not in ["email", "filename", "registry", "xmpid"]:
                    raise AnalyzerRunException(f"Unknown Type: {type_}")

                uri = f"/api/dfi/search/ioc/{type_}?keyword={value}"
            else:
                raise AnalyzerRunException()

        elif self.analysis_type == "iocdb_search":
            uri = f"/api/iocdb/search?keyword={self.observable_name}"

        elif self.analysis_type == "repdb_search":
            uri = f"/api/repdb/search?keyword={self.observable_name}"

        else:
            raise AnalyzerConfigurationException(
                f"analysis type: '{self.analysis_type}' not suported."
                "Supported are: 'dfi_search', 'iocdb_search', 'repdb_search'."
            )

        try:
            response = requests.get(self.base_url + uri, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise AnalyzerRunException(e)
        result = response.json()
        if (
            self.analysis_type == "dfi_search"
            and self.observable_classification == self.ObservableTypes.HASH
        ):
            result["hash_type"] = self.hash_type

        if self.generic_identifier_mode == "auto":
            result["type_of_generic"] = self.type_of_generic()

        return result

    @classmethod
    def _monkeypatch(cls):
        patches = [
            if_mock_connections(
                patch(
                    "requests.get",
                    return_value=MockResponse({}, 200),
                ),
            )
        ]
        return super()._monkeypatch(patches=patches)
