import sublime
import sublime_plugin
import subprocess
import sys

class TransmitDocksendCompiledStyleCommand(sublime_plugin.TextCommand):
	def run(self, edit, connection=False):
		alt_file = None
		file_name = self.view.file_name()
		
		if file_name.endswith(".scss"):
			alt_file = file_name.replace(".scss", ".css")

		if connection == 'active':
			if alt_file is None:
				script = """
				on run
				tell application "Transmit"
					tell current tab of front document
						tell remote browser
							upload item at path "{0}"
						end tell
					end tell
				end tell
				end run
				"""
			else:
				script = """
				on run
				tell application "Transmit"
					tell current tab of front document
						tell remote browser
							upload item at path "{0}"
							upload item at path "{1}"
						end tell
					end tell
				end tell
				end run
				"""

		else:
			if alt_file is None:
				script = """
				on run
					ignoring application responses
						tell application "Transmit"
							open POSIX file "{0}"
						end tell
					end ignoring
				end run
				"""
			else:
				script = """
				on run
					ignoring application responses
						tell application "Transmit"
							open POSIX file "{0}"
							open POSIX file "{1}"
						end tell
					end ignoring
				end run
				"""

		if alt_file is None:
			script_str = script.format(self.view.file_name())
		else:
			script_str = script.format(self.view.file_name(), alt_file)

		#sys.stdout.write(script_str)

		proc = subprocess.Popen(
			["osascript", "-e", script_str], 
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT
		)

class TransmitDocksendCompiledStyleFileCommand(sublime_plugin.TextCommand):
	def run(self, edit, connection=False):
		alt_file = None
		file_name = self.view.file_name()
		
		if file_name.endswith(".scss"):
			file_parts = file_name.rpartition("/")
			#file_parts[2] = "fake-style.css"
			alt_file = file_parts[0] + "/style.css"

		if connection == 'active':
			if alt_file is None:
				script = """
				on run
				tell application "Transmit"
					tell current tab of front document
						tell remote browser
							upload item at path "{0}"
						end tell
					end tell
				end tell
				end run
				"""
			else:
				script = """
				on run
				tell application "Transmit"
					tell current tab of front document
						tell remote browser
							upload item at path "{0}"
							upload item at path "{1}"
						end tell
					end tell
				end tell
				end run
				"""

		else:
			if alt_file is None:
				script = """
				on run
					ignoring application responses
						tell application "Transmit"
							open POSIX file "{0}"
						end tell
					end ignoring
				end run
				"""
			else:
				script = """
				on run
					ignoring application responses
						tell application "Transmit"
							open POSIX file "{0}"
							open POSIX file "{1}"
						end tell
					end ignoring
				end run
				"""
				
		if alt_file is None:
			script_str = script.format(self.view.file_name())
		else:
			script_str = script.format(self.view.file_name(), alt_file)

		#sys.stdout.write(script_str)

		proc = subprocess.Popen(
			["osascript", "-e", script_str], 
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT
		)
