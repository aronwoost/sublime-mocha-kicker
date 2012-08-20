import sublime, sublime_plugin, ntpath

# does not work sublime_plugin.WindowCommand, no clue why
class SaveSpecsFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# all open view (i.e. tabs)
		views = self.view.window().views()
		for v in views:
			# check if the filename start with "test."
			if ntpath.basename(v.file_name())[0:5] == "test.":
				# print(ntpath.basename(v.file_name()))
				v.run_command("save")