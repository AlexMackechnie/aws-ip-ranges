upgrade_pip:
	pip install --upgrade pip

install_freeze_tools:
	pip install --upgrade pip-tools

install_build_tools:
	pip install --upgrade build

install_dev: upgrade_pip
	pip install -e . --config-settings editable_mode=strict



