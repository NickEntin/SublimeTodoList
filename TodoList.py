import sublime, sublime_plugin

class TodoList(sublime_plugin.EventListener):
	def on_modified(self, view):
		items = view.find_all("TODO")
		view.add_regions("todo", items, "todo", "bookmark", sublime.HIDDEN)
