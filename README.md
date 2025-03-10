<img src="static_intel/intel_owl_positive.png" width=547 height=150 alt="Intel Owl"/>


[![GitHub release (latest by date)](https://img.shields.io/github/v/release/intelowlproject/IntelOwl)](https://github.com/intelowlproject/IntelOwl/releases)
[![GitHub Repo stars](https://img.shields.io/github/stars/intelowlproject/IntelOwl?style=social)](https://github.com/intelowlproject/IntelOwl/stargazers)
[![Docker](https://img.shields.io/docker/pulls/intelowlproject/intelowl)](https://hub.docker.com/repository/docker/intelowlproject/intelowl)
[![Twitter Follow](https://img.shields.io/twitter/follow/intel_owl?style=social)](https://twitter.com/intel_owl)
[![Official Site](https://img.shields.io/badge/official-site-blue)](https://intelowlproject.github.io)


[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/intelowlproject/IntelOwl.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/intelowlproject/IntelOwl/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/intelowlproject/intelowl/badge)](https://www.codefactor.io/repository/github/intelowlproject/intelowl)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/intelowlproject/IntelOwl/branch/master/graph/badge.svg?token=R097M4TYA6)](https://codecov.io/gh/intelowlproject/IntelOwl)
[![Build & Tests](https://github.com/intelowlproject/IntelOwl/workflows/Build%20&%20Tests/badge.svg)](https://github.com/intelowlproject/IntelOwl/actions)


# Intel Owl

Do you want to get **threat intelligence data** about a malware, an IP or a domain? Do you want to get this kind of data from multiple sources at the same time using **a single API request**?

You are in the right place!

Intel Owl is an Open Source Intelligence, or OSINT solution to get threat intelligence data about a specific file, an IP or a domain from a single API at scale. It integrates a number of analyzers available online and is for everyone who needs a single point to query for info about a specific file or observable.

### Features

- Provides enrichment of threat intel for malware as well as observables (IP, Domain, URL and hash).
- This application is built to **scale out** and to **speed up the retrieval of threat info**.
- It can be integrated easily in your stack of security tools ([pyintelowl](https://github.com/intelowlproject/pyintelowl)) to automate common jobs usually performed, for instance, by SOC analysts manually.
- Intel Owl is composed of **analyzers** that can be run to retrieve data from external sources (like VirusTotal or AbuseIPDB) or to generate intel from internal analyzers (like Yara or Oletools)
- API written in Django and Python 3.8.
- Inbuilt frontend client: **[IntelOwl-ng](https://github.com/intelowlproject/IntelOwl-ng)** provides features such as dashboard, visualizations of analysis data, easy to use forms for requesting new analysis, etc. [Live Demo](https://intelowlclient.firebaseapp.com/).

## Documentation

[![Documentation Status](https://readthedocs.org/projects/intelowl/badge/?version=latest)](https://intelowl.readthedocs.io/en/latest/?badge=latest)

Documentation about IntelOwl installation, usage, configuration and contribution can be found at https://intelowl.readthedocs.io/.

## Blog posts

To know more about the project and it's growth over time, you may be interested in reading the following:

- [Intel Owl on Daily Swig](https://portswigger.net/daily-swig/intel-owl-osint-tool-automates-the-intel-gathering-process-using-a-single-api)
- [Honeynet: v1.0.0 Announcement](https://www.honeynet.org/?p=7558)
- [Certego Blog: First announcement](https://www.certego.net/en/news/new-year-new-tool-intel-owl/)

## Available services or analyzers

You can see the full list of all available analyzers in the [documentation](https://intelowl.readthedocs.io/en/latest/Usage.html#available-analyzers) or [live demo](https://intelowlclient.firebaseapp.com/pages/analyzers/table).

| Type                                               | Analyzers Available                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inbuilt modules                                    | - Static Document, RTF, PDF, PE, Generic File Analysis<br/> - Strings analysis with ML<br/> - PE Emulation with Speakeasy<br/> - PE Signature verification<br/> - PE Capabilities Extraction<br/> - Emulated Javascript Analysis<br/> - Android Malware Analysis<br/> - SPF and DMARC Validator<br/> - more... |
| External services                                  | - GreyNoise v2<br/> - Intezer Scan<br/>  - VirusTotal v2+v3<br/>  - HybridAnalysis<br/>  - Censys.io<br/>  - Shodan<br/>  - AlienVault OTX<br/>  - Threatminer<br/>  - Abuse.ch<br/>  - many more..                                                                                                            |
| Free modules that require additional configuration | - Cuckoo (requires at least one working Cuckoo instance)<br/>  - MISP (requires at least one working MISP instance)<br/>  - Yara (Community, Neo23x0, Intezer, McAfee rules are already available. There's the chance to add your own rules)                                                                   |

## Premium support 
<img src="static_intel/xscode-banner.png" width="600" height="120" alt="xscode: Get Support"/><br/>
_For urgent issues and priority support, visit [https://xscode.com/intelowlproject/IntelOwl](https://xscode.com/intelowlproject/IntelOwl)._

## Legal notice

You as a user of this project must review, accept and comply with the license
terms of each downloaded/installed package listed below. By proceeding with the
installation, you are accepting the license terms of each package, and
acknowledging that your use of each package will be subject to its respective
license terms.

[osslsigncode](https://github.com/develar/osslsigncode),
[PyExifTool](https://github.com/sylikc/pyexiftool),
[Exiftool package](https://exiftool.org/#license),
[stringsifter](https://github.com/fireeye/stringsifter),
[peepdf](https://github.com/jesparza/peepdf),
[pefile](https://github.com/erocarrera/pefile),
[oletools](https://github.com/decalage2/oletools),
[XLMMacroDeobfuscator](https://github.com/DissectMalware/XLMMacroDeobfuscator),
[MaxMind-DB-Reader-python](https://github.com/maxmind/MaxMind-DB-Reader-python),
[pysafebrowsing](https://github.com/Te-k/pysafebrowsing),
[google-web-risk](https://github.com/googleapis/python-webrisk),
[PyMISP](https://github.com/MISP/PyMISP),
[OTX-Python-SDK](https://github.com/AlienVault-OTX/OTX-Python-SDK),
[yara-python](https://github.com/VirusTotal/yara-python),
[GitPython](https://github.com/gitpython-developers/GitPython),
[Yara community rules](https://github.com/Yara-Rules),
[StrangerealIntel Daily Ioc Yara rules](https://github.com/StrangerealIntel/DailyIOC),
[Neo23x0 Yara rules](https://github.com/Neo23x0/signature-base),
[Intezer Yara rules](https://github.com/intezer/yara-rules),
[McAfee Yara rules](https://github.com/advanced-threat-research/Yara-Rules),
[Stratosphere Yara rules](https://github.com/stratosphereips/yara-rules),
[FireEye Yara rules](https://github.com/fireeye/red_team_tool_countermeasures),
[ReversingLabs Yara rules](https://github.com/reversinglabs/reversinglabs-yara-rules),
[Samir Yara rules](https://github.com/sbousseaden/YaraHunts),
[InQuest Yara rules](https://github.com/InQuest/yara-rules),
[APKiD](https://github.com/rednaga/APKiD/blob/master/LICENSE.COMMERCIAL),
[Box-JS](https://github.com/CapacitorSet/box-js/blob/master/LICENSE),
[Capa](https://github.com/fireeye/capa/blob/master/LICENSE.txt),
[Quark-Engine](https://github.com/quark-engine/quark-engine),
[IntelX](https://intelx.io/terms-of-service),
[Speakeasy](https://github.com/fireeye/speakeasy),
[Checkdmarc](https://github.com/domainaware/checkdmarc),
[Manalyze](https://github.com/JusticeRage/Manalyze),
[Qiling](https://github.com/qilingframework/qiling),
[Renderton](https://github.com/GoogleChrome/rendertron/blob/main/LICENSE)
[PyCTI](https://github.com/OpenCTI-Platform/client-python/blob/master/LICENSE),
[PyHashlookup](https://github.com/CIRCL/PyHashlookup),
[PyPDNS](https://github.com/CIRCL/PyPDNS)

## Acknowledgments

### Sponsors

This project was created and will be upgraded thanks to the following organizations:

#### Certego
<a href="https://www.certego.net"> <img style="margin-right: 2px" width=176 height=50 src="static_intel/Certego.png" alt="Certego Logo"/> </a>

#### The Honeynet Project
<a href="https://www.honeynet.org"> <img style="border: 0.2px solid black" width=115 height=150 src="static_intel/honeynet_logo.png" alt="Honeynet.org logo"> </a>

Since its birth, this project has been participating in the [Google Summer of Code](https://summerofcode.withgoogle.com/) (GSoC) under the Honeynet Project!

Project Summaries and/or in-development projects:
* 2020: [Eshaan Bansal](https://twitter.com/eshaan7_): [IntelOwl Work Product](https://www.honeynet.org/2020/08/26/gsoc-2020-work-product%e2%80%8a-%e2%80%8aintel-owl/)
* 2021: 
  * [Sarthak Khattar](https://twitter.com/Mr_Momo07): [IntelOwl Improvements](https://www.honeynet.org/2021/08/20/gsoc-2021-project-summary-intelowl-improvements/)
  * [Shubham Pandey](https://twitter.com/imshubham31): [IntelOwl Connectors Manager and Integrations](https://www.honeynet.org/2021/08/20/gsoc-2021-project-summary-intelowl-connectors-manager-and-integrations/)

Stay tuned for the upcoming GSoC! Join the [Honeynet Slack chat](https://gsoc-slack.honeynet.org/) for more info.

#### Docker
In 2021 IntelOwl joined the official [Docker Open Source Program](https://www.docker.com/blog/expanded-support-for-open-source-software-projects/)

## About the author and maintainers

Feel free to contact the main developers at any time in Twitter:
- [Matteo Lodi](https://twitter.com/matte_lodi): Author and creator
- [Eshaan Bansal](https://twitter.com/eshaan7_): Principal maintainer
