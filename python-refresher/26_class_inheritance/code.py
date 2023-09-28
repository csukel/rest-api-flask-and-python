class Device():
	def __init__(self, name, connected_by) -> None:
		self.name = name
		self.connected_by = connected_by
		self.connected = True
	
	def __str__(self) -> str:
		return f"Device {self.name!r} ({self.connected_by})"
	
	def dicsonnect(self):
		self.connected = False
		print("Disconnected.")

# printer = Device("Printer", "USB")
# print(printer)
# printer.dicsonnect()

class Printer(Device):
	def __init__(self, name, connected_by, capacity) -> None:
		super().__init__(name, connected_by)
		self.capacity = capacity
		self.remaining_pages = capacity

	def print(self, pages=1):
		if not self.connected:
			print("Your printer is not connected")
		
		if self.remaining_pages - pages > 0:
			self.remaining_pages -= pages
			print(f"Printing {pages} pages.")
		else:
			print(f"The printer has less pages remaining ({self.remaining_pages}) in comparison with the provided value ({pages})")

	def __str__(self) -> str:
		return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
	
printer = Printer("Brother MCF 410", "USB", 100)

print(printer)
printer.print(1)
print(printer)
printer.print(1000)
