import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World! xxxxxx\n")

class Rot13Command(sublime_plugin.TextCommand):  
    def run(self, edit):  
        for region in self.view.sel():  
            if not region.empty():  
                # Get the selected text  
                s = self.view.substr(region)  
                # Transform it via rot13  
                s = s.encode('rot13')  
                # Replace the selection with transformed text  
                self.view.replace(region, s)

# Extends TextCommand so that run() receives a View to modify.  
class DuplicateCommand(sublime_plugin.TextCommand):  
    def run(self, edit):  
        # Walk through each region in the selection  
        for region in self.view.sel():  
            # Only interested in empty regions, otherwise they may span multiple  
            # lines, which doesn't make sense for this command.  
            print(region)
            if region.empty():  
                # Expand the region to the full line it resides on, excluding the newline  
                line = self.view.line(region)  
                # Extract the string for the line, and add a newline  
                lineContents = self.view.substr(line) + '\n'  
                # Add the text at the beginning of the line
                self.view.insert(edit, line.begin(), lineContents)


