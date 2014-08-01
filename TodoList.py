import sublime, sublime_plugin

class TodoList(sublime_plugin.EventListener):
	def scan_file(self, view):
		items = view.find_all("TODO")
		view.add_regions("todo", items, "todo", "bookmark", sublime.HIDDEN)

	def on_modified(self,view):
		self.scan_file(view);

	def on_load(self,view):
		self.scan_file(view);
