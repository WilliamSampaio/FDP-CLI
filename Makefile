APP_NAME=fdp-cli

SCRIPTS_INSTALL_DIR = /usr/local/bin

.PHONY: all install uninstall

all: install

install:
	@echo "📦 Installing $(APP_NAME) in $(SCRIPTS_INSTALL_DIR)..."
	@sudo install -Dm 0755 fdp-cli.py $(SCRIPTS_INSTALL_DIR)/fdp-cli
	@sudo install -Dm 0755 fdp-configure.py $(SCRIPTS_INSTALL_DIR)/fdp-configure
	@echo "✅ Installation complete. Now you can use the command '$(APP_NAME)' directly. Reload your shell."
	@echo "Reload your terminal to add scripts to your PATH if the commands are still not found."

uninstall:
	@echo "🗑️ Uninstalling $(APP_NAME) from $(SCRIPTS_INSTALL_DIR)..."
	@sudo rm $(SCRIPTS_INSTALL_DIR)/fdp-cli
	@sudo rm $(SCRIPTS_INSTALL_DIR)/fdp-configure
	@echo "✅ Uninstallation complete."
