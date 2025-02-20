# Changelog


This changelog is auto generated by scanning the commit history.
Commits have to follow following convention: https://www.conventionalcommits.org/en/v1.0.0/

## Version Unreleased

### Bug Fixes

- Pcan logs for macos
- Make sure the action is triggered correctly ([#187](https://github.com/orhun/git-cliff/issues/187))

### Miscellaneous Tasks

- Bump pykiso-python-uds from 3.0.0 to 3.0.1 ([#163](https://github.com/orhun/git-cliff/issues/163))
- Bump pytest from 7.1.2 to 7.1.3 ([#155](https://github.com/orhun/git-cliff/issues/155))
- Debian:11.0
- Bump black from 22.3.0 to 22.8.0 ([#154](https://github.com/orhun/git-cliff/issues/154))
- Bump invoke from 1.7.1 to 1.7.3
- Bump pylink-square from 0.14.2 to 0.14.3
- Bump black from 22.8.0 to 22.10.0 ([#179](https://github.com/orhun/git-cliff/issues/179))
- Bump coverage from 6.4.4 to 6.5.0 ([#181](https://github.com/orhun/git-cliff/issues/181))
- Bump pytest-mock from 3.8.2 to 3.10.0 ([#178](https://github.com/orhun/git-cliff/issues/178))
- Bump tabulate from 0.8.10 to 0.9.0
- Bump pytest from 7.1.3 to 7.2.0
- Bump pytest-cov from 3.0.0 to 4.0.0
- Bump importlib-metadata from 4.12.0 to 5.0.0 ([#166](https://github.com/orhun/git-cliff/issues/166))

### New Features

- Ensure default behaviour when (suite case) id is 0 ([#177](https://github.com/orhun/git-cliff/issues/177))
- Process connector ([#165](https://github.com/orhun/git-cliff/issues/165))
- Add stepreport example ([#192](https://github.com/orhun/git-cliff/issues/192))
- Make release 0.20.0 ([#194](https://github.com/orhun/git-cliff/issues/194))

### Ci[dependabot]

- Update to monthly PRs ([#180](https://github.com/orhun/git-cliff/issues/180))

## Version 0.19.3 (2022-09-16)

### Bug Fixes

- Handle case odx_file_path parameter is type of bool ([#158](https://github.com/orhun/git-cliff/issues/158))
- Step report problem with inspect module in python>=3.8 ([#160](https://github.com/orhun/git-cliff/issues/160))

### Miscellaneous Tasks

- Release 0.19.3 ([#161](https://github.com/orhun/git-cliff/issues/161))

### New Features

- Write stderr to file when file logging is activated ([#159](https://github.com/orhun/git-cliff/issues/159))

## Version 0.19.2 (2022-09-13)

### Bug Fixes

- Changelog only triggered on master
- Cleanup auxiliary properly by removing them from sys.modules ([#147](https://github.com/orhun/git-cliff/issues/147))
- Fix double Logging with --junit option
- Update logging initializer so that internal logs are always logged in file

### Miscellaneous Tasks

- Add jinja2 for step reporter dependency
- [**breaking**] Release 0.19.2

### New Features

- Select test case with regex ([#146](https://github.com/orhun/git-cliff/issues/146))

### Refactorings

- Small fixes

## Version 0.19.1 (2022-09-02)

### Bug Fixes

- Readthedocs requirements

### Miscellaneous Tasks

- Bump pre-commit from 2.19.0 to 2.20.0
- Bump coverage from 5.5 to 6.4.4
- Bump pytest-mock from 3.7.0 to 3.8.2
- Bump pylink-square from 0.12.0 to 0.14.2 ([#137](https://github.com/orhun/git-cliff/issues/137))
- Update click ([#143](https://github.com/orhun/git-cliff/issues/143))
- Release 0.19.1 ([#144](https://github.com/orhun/git-cliff/issues/144))

### New Features

- Add start and stop uds tester present sender ([#131](https://github.com/orhun/git-cliff/issues/131))
- Add cc_serial connector ([#124](https://github.com/orhun/git-cliff/issues/124))

### Refactorings

- Restructure the documentation

### Ci

- Replace auto-changelog

## Version 0.19.0 (2022-08-30)

### Bug Fixes

- Multiple yaml logging
- Hanging ci and rework mp aux and proxy pytest
- Virtual test fail
- Skip suite tests when setup fails
- Redefine jenkins resources & timeouts
- Correct AttributeError when setUpClass failed for junit report generation ([#120](https://github.com/orhun/git-cliff/issues/120))
- MarkupSafe
- Update pykitest example
- Step report ci issues([#134](https://github.com/orhun/git-cliff/issues/134))
- Replace dependabot to .github ([#133](https://github.com/orhun/git-cliff/issues/133))

### Documentation

- Add tools section and remove tools from coverage
- Align dependencies in NOTICE.md ([#90](https://github.com/orhun/git-cliff/issues/90))
- Fix dead links and rework formatting ([#105](https://github.com/orhun/git-cliff/issues/105))
- Extend contribution parts with DoD hints ([#94](https://github.com/orhun/git-cliff/issues/94))

### Miscellaneous Tasks

- Fix issues induced by tmp_path fixture
- Fix docstring
- Rename show-tag CLI to pykiso-tags
- Bump lxml from 4.9.0 to 4.9.1 ([#88](https://github.com/orhun/git-cliff/issues/88))

### New Features

- Add show tag script for test information analysis
- Detect test collection errors and abort execution
- Implement double threaded auxiliary interface ([#74](https://github.com/orhun/git-cliff/issues/74))
- Make DuT DT-aux capable ([#77](https://github.com/orhun/git-cliff/issues/77))
- Add a tester present sender to uds auxiliary ([#87](https://github.com/orhun/git-cliff/issues/87))
- ComAux ability to handle reception buffer ([#86](https://github.com/orhun/git-cliff/issues/86))
- Improve error reporting in test case execution ([#111](https://github.com/orhun/git-cliff/issues/111))
- Improve error reporting in test case execution ([#111](https://github.com/orhun/git-cliff/issues/111)) ([#91](https://github.com/orhun/git-cliff/issues/91))
- Adapt UDS auxiliary and server to the dt auxiliary interface ([#114](https://github.com/orhun/git-cliff/issues/114))
- Add dependabot to manage our fixed dependencies ([#121](https://github.com/orhun/git-cliff/issues/121))
- Add new logging strategy ([#122](https://github.com/orhun/git-cliff/issues/122))
- Step report ([#101](https://github.com/orhun/git-cliff/issues/101))
- Make release 0.19.0 ([#130](https://github.com/orhun/git-cliff/issues/130))

### Refactorings

- Migrate recorder to DT-aux interface ([#80](https://github.com/orhun/git-cliff/issues/80))
- Adapt acroname aux to dt interface ([#84](https://github.com/orhun/git-cliff/issues/84))
- Adapt instrument aux to dt interface ([#85](https://github.com/orhun/git-cliff/issues/85))

### Testing

- Add tests for show-tag
- Increase coverage
- Try to fix get_yaml_files test

### Bugfix

- Fix/adapt socketcan connectors to be agnostic ([#89](https://github.com/orhun/git-cliff/issues/89))
- Adapt rtt connector to create log folder if does not exist ([#92](https://github.com/orhun/git-cliff/issues/92))
- Do not wait for an UDS response in tester present sender ([#113](https://github.com/orhun/git-cliff/issues/113))

### Chor

- Pykiso python uds 3 0 0 ([#119](https://github.com/orhun/git-cliff/issues/119))

## Version 0.18.0 (2022-06-08)

### Documentation

- Add whats new for 0.17.0
- Make usage of TestSuite elements more visible
- Add quality goals

### New Features

- Make bus error warnings switchable for pcan
- Set up badges
- Multiple yaml in CLI
- Rework pcan trace configuration in connector
- Add pykiso to pytest tool ([#62](https://github.com/orhun/git-cliff/issues/62))
- Make the proxy agnostic of transitioning messages
- Create base class for test ([#61](https://github.com/orhun/git-cliff/issues/61))
- Make release 0.18.0 ([#72](https://github.com/orhun/git-cliff/issues/72))

## Version 0.17.0 (2022-05-04)

### Bug Fixes

- Qsize() not available for macos x
- Pytest config and flake8 excludes
- Remove --dev option (default for poetry)
- Restrict markupsafe versions and cleanup docs
- Use coverage coonfig from pyproject.toml
- Point to pykiso-python-uds-alpha for PYPI

### Documentation

- Remove not maintained 'list of limitations' section
- Add section whats new ([#38](https://github.com/orhun/git-cliff/issues/38))
- Replace all occurences of pipenv with poetry
- Rework getting_started

### New Features

- Update to new release 0.17.0

### Refactorings

- [**breaking**] Change variant decorator
- [**breaking**] Change variant decorator
- Replace all setuptools-based files with poetry

### Testing

- Add missing unittests

### Bugfix

- Remove warning in unittests
- Remove warning in unittests

### Ci

- Update pipeline with poetry
- Skip poetry install
- Add poetry installation

## Version 0.16.0 (2022-03-22)

### Bug Fixes

- Wait for logger thread to quit gracefully before closing segger channel ([#28](https://github.com/orhun/git-cliff/issues/28))

### Documentation

- Change auto changelog tool ([#30](https://github.com/orhun/git-cliff/issues/30))

### New Features

- Add uptime for pcan inside python-can
- Expose yaml and cli configuration to user test cases/suites
- Add uptime for pcan inside python-can
- [**breaking**] Restore yaml loader in config parser ([#31](https://github.com/orhun/git-cliff/issues/31))
- Raise an exception when auxiliary failed at instance creation ([#33](https://github.com/orhun/git-cliff/issues/33))
- Update to new release 0.16.0 ([#34](https://github.com/orhun/git-cliff/issues/34))

### Ci

- Github-action for codecov ([#27](https://github.com/orhun/git-cliff/issues/27))
- Add skip lock for pipenv to prevent hangup
- Add skip lock for pipenv to prevent hangup

## Version 0.15.1 (2022-02-17)

### Documentation

- Add links for how to create an auxiliary and connector ([#17](https://github.com/orhun/git-cliff/issues/17))

### Testing

- Make test reliable ([#18](https://github.com/orhun/git-cliff/issues/18))

## Version 0.15.0 (2022-02-11)

### Documentation

- Restructure docs ([#14](https://github.com/orhun/git-cliff/issues/14))
- Autogen changelog ([#15](https://github.com/orhun/git-cliff/issues/15))

### New Features

- Update to new release 0.15 ([#13](https://github.com/orhun/git-cliff/issues/13))

## Version 0.15.0 (in addition)

Features:
- add capability to not automatically start an auxiliary and let the user do it (auto_start parameter for threaded auxiliaries only)
- add socket can connector with trc file logger
- add bitrate switch to every can bus connector
- add copycat capability (beta feature) for "threaded" auxiliaries
- Add multiprocessing and proxy capability to the recorder auxiliary

Bugfix:
- correct random fail issue from proxy auxiliary unit test
- remove error handling during flashing in flash_jlink (handled by auxiliary)

Changes:
- refactor test_case, test_suite, test_message_handler module

## Version 0.14.0

Features:
- add test name on failure (print: test name, description and reason)
- manage RTT connector resource consumption using rtt_log_speed parameter
- repeat testCases upon failure (x run, 1 successful -> ok & go)
- repeat testCases for stability test (x run, 1 failure -> not ok & go)
- add reset function and decorator to RTT connector
- add functionalities to recorder auxiliary

Changes:
- move error messages from python-can 4.0.0 into log level debug
- add timeout in the receive method in order to to send the signal to the GIL to change thread
- add Repeat test upon failure examples and documentation

Bugfix:
- Empty multiprocessing queue in instance deletion to avoid auxiliary hanging issues(workaround)

## Version 0.13.1 (internal release)

Bugfix:
- correct junit reporting instability by flushing StreamHandler at each test cases start

Features:
- *BREAKING CHANGE*: Improve test fixture labeling by introducing branch_level params

## Version 0.13.0 (internal release)

Changes:
- set message reception size to buffer size in CCRttSegger if raw is set
- Change pykiso import order for new vsc intellisense approach

Bugfix:
- fix wrong exit code return when an exception is raised at suite collection level

Features:
- add BannerTestResult to show test execution results in a banner

## Version 0.12.1 (internal release)

Bugfix:
- Variant skipped but case_setup and case_teardown kept executed

Features:
- add capability to read target memory to jlink connector

## Version 0.12.0 (internal release)

Features:
- add PATTERN argument in CLI to overwrite the test_filter_pattern


## Version 0.11.1 (internal release)

Changes:
- remove brainstem libs because of installations conflicts

## Version 0.11.0 (internal release)

Changes:
- Add external brainstem package for local installation

Features:
- add record auxiliary
- add acroname robot auxiliary
- add auxiliary to control acroname usb hubs
- add multiprocessing based auxiliary interface
- add multiprocessing proxy auxiliary version
- add multiprocessing proxy channel version
- add simple auxiliary interface

Changes:
- put thread and multiprocessing based auxiliary interface in a dedicated folder
- make acroname auxiliary inherit from SimpleAuxiliaryInterface
- make instrument auxiliary inherit from SimpleAuxiliaryInterface

## Version 0.10.3 (internal release)

Changes:
- Move back to threading RLock instead of multiprocessing one for CChannel interface

## Version 0.10.2 (internal release)

Features:
- add variant option to pykiso command
- add package requirements into the yaml file (version check)

Bugfix:
- improve proxy auxiliary stability
- fix sporadic issue seen when CTRL+C is pressed(UnboundLocalError)


## Version 0.10.1 (internal release)

Features:
- add reset in CCRttSegger if the debugger is halted

Bugfix:
- explicitly cast fdx connector and flasher params
- set CCRttSegger serial_no to None if the given one is not an int
- fix flash-lauterbach to wait properly till scripts are executed.


## Version 0.10.0

Features:
- add capability to generate a trace file for proxy auxiliary
- add PCAN connector
- add Vector-CAN connector
- Run proxy aux on a different process to improve cpu utilization.
  E.g. cycle time of network status message has less jitter.

Bugfix:
- failing attempt to quit trace32 will not affect the pykiso test result
- resolve folder naming conflicts when parsing the config file
- flash-jlink didn't connect to given serial number

## Version 0.9.4 (internal release)

Features:
- introduce is_pausable flag to force an auxiliary to wait
- add logger activation for all auxiliaries

Changes:
- make instrument control auxiliary respect auxiliary interface
- deactivate all non-pykiso loggers

Bugfix:
- log any error when loading multiple testsuites

## Version 0.9.3 (internal release)

Features:
- add environment variable casting for float, bool, etc.

Changes:
- refactor parse_config and move it in config_parser.py

Bugfix:
- fix connection issues when t32 is already running
- fix connection issues when t32 executable is not able to start

## Version 0.9.2 (internal release)

Features:
- add environment variable casting for integer-like strings
- warn user and raise NotImplementedError when an auxiliary is not proxy compatible
- add templates for all available features, auxiliaries and connectors

Bugfix:
- correct issue on InstrumentControlAuxiliary using 'Rohde&Schwarz' instrument name
- correct error when opening cc_tcp_ip with the wrong IP address

## Version 0.9.1 (internal release)

Bugfix:
- fix log capability

## Version 0.9.0 (internal release)

Features:
- add tcp/ip socket connector
- add SOCKET interface to instrument_control_cli
- add stdout writing in junit report
- add line number in logging message format

Bugfix:
- correct issue on proxy connector/auxiliary deletion phase
- correct issue on proxy auxiliary regarding late auxiliary import magic
- correct performance issues when auxiliaries are suspended
- correct validation mechanism in InstrumentControlAuxiliary

## Version 0.8.1 (internal release)

Features:
- add robot framework version of proxy auxiliary
- add robot framework version of instrument control auxiliary
- add RTT log reading in cc_rtt_segger

Changes:
- adapt robot communication auxiliary keywords

Bugfix:
- remove all sphinx documentation generation warnings

## Version 0.8.0 (internal release)

Features:
- DUTAuxiliary can be used with the robotframework to control the TestApp
- add new VISA connectors in cc_visa for VISA communication via serial and TCP/IP
- add new instrument_control_auxiliary that uses the VISA connectors to communicate with instruments.
- add two examples and a command line interface to control the instrument.
- the test reference (eg: JAMA) can be assigned

Changes:
- improve code for robot package
- Update AuxiliaryInterface run method in order to avoid None value in queue_out.

Bugfix:
- adapt return values from receive_message method for robot communication auxiliary

Tests:
- add unit tests for framework package (interface, loader and communication aux)

## Version 0.7.0 (internal release)

Features:
- add auxiliary resume and suspend capabilities

## Version 0.6.1 (internal release)

Bugfix:
- fix issue in config parser when entity name matches folder name

## Version 0.6.0 (internal release)

Features:
- modify define_test_parameters decorator in order to have parametrized timeout for each test fixtures.
- add reset functionality for the cc_fdx_lauterbach

Changes:
- adapt ExampleAuxiliary timeout value

Bugfix
- fix test case run scenario for DUT simulation
- fix import issue for test_suite_virtual (UDP server has to be first)

Tests:
-add pytest regarding define_test_parameters decorator modification

## Version 0.5.1 (internal release)

Changes:
- track python guidelines
- split file test_factory_and_execution.py into test_execution and config_registry
- restructured files into folders test_coordinator and test_setup

Bugfix
- fix parsing of environment variables in the connectors config

## Version 0.5.0 (internal release)

Features:
- add proxy connector
- add proxy auxiliary
- allow relative paths in yaml file
- added automatic detection of Vector Boxes' serial number
- add nested yaml capability (introduce !include tag)

Changes:
- add docstrings and typehints for several connector implementation
- remove usage of timeout parameter for cc_send method in CChannel class
- add parameter kwargs for cc_send method in CChannel class

Tests:
- add pytest for proxy connector
- add pytest for proxy auxiliary
- adapt test_simulated_auxiliary (use of sys.exit)
- set pytest logging level to INFO
- add test for cli.py

## Version 0.4.0 (internal release)

Features:

Changes:

Bugfixes:
- fixed bug when generating junit report and reports folder does not exist
- fixed bug Vector serial number with leading zeros


## Version 0.3.0 (internal release)

Changes:
- adding module-specific log in pykiso

Bugfixes:
- fixed bug enum34 package during developers installation

Tests:
- adapt tests which uses log to use module-specific logs
- correct tests for test_factory_and_execution module

## Version 0.2.0 (internal release)

Features:
- add cli option for junit report generation
- add automated jenkins run of the dummy.yaml file
- add reports folder in which the junit reports are saved
- add the ability to use environment variables in YAML files

Changes:
- modify define_test_parameters decorator to get the test case infos in the test results and test reports.
- Implement the catch of KeyboardInterrupt exception during pykiso execution

Bugfixes:
- fixed a bug in the flash_Lauterbach connector
- fixed reading of the messages from TestApp on pykiso side

Tests :
- add tests for test_factory_and_execution with different reporting options.

## Version 0.1.0 (internal release)

Features:
- add Device Under Test Auxiliary (DUT)
- add PCAN connector
- add Segger RTT connector (communication channel)
- add dummy jenkins file

Changes:
- add example/configuration file for Segger RTT channel (flasher and communication)
- update sphinx documentation

Bugfixes:
- fix message segmentation issue on reception for Segger RTT connector
- fix management of LOG message type from test protocol
- fix flash procedure for Segger RTT connector (flasher channel)
- fix typo issues

Tests :
- add unit tests for DUT auxiliary
- add unit tests for Segger RTT connector
- adapt integration tests (using virtual auxiliary) for DUT auxiliary


## Version 0.0.0

- Initial version

<!-- generated by git-cliff -->
