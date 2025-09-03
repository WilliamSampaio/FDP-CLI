APP_NAME=fdp-cli

SCRIPTS_INSTALL_DIR = /usr/local/bin
FILES_INSTALL_DIR = /usr/local/share

.PHONY: all install uninstall

all: install

install:
	@echo "📦 Installing $(APP_NAME) in $(SCRIPTS_INSTALL_DIR)..."
	@sudo install -Dm 0755 fdp-cli.py $(SCRIPTS_INSTALL_DIR)/fdp-cli
	@sudo install -Dm 0755 fdp-configure.py $(SCRIPTS_INSTALL_DIR)/fdp-configure
	@echo "📦 Installing $(APP_NAME) in $(SCRIPTS_INSTALL_DIR)..."
	@sudo mkdir -p $(FILES_INSTALL_DIR)/$(APP_NAME)
	@sudo cp fdp.yaml.example $(FILES_INSTALL_DIR)/$(APP_NAME)/
	@echo "✅ Installation complete. Now you can use the command '$(APP_NAME)' directly. Reload your shell."
	@echo "Reload your terminal to add scripts to your PATH if the commands are still not found."

uninstall:
	@echo "🗑️ Uninstalling $(APP_NAME) from $(SCRIPTS_INSTALL_DIR)..."
	@sudo rm $(SCRIPTS_INSTALL_DIR)/fdp-cli
	@sudo rm $(SCRIPTS_INSTALL_DIR)/fdp-configure
	@echo "🗑️ Uninstalling $(APP_NAME) from $(FILES_INSTALL_DIR)..."
	@sudo rm -rf $(FILES_INSTALL_DIR)/$(APP_NAME)
	@echo "✅ Uninstallation complete."
