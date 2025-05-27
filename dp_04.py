from abc import abstractmethod
class Machine:
    def print(self,document):
        raise NotImplementedError
    def fax(self , document):
        raise NotImplementedError
    def scan(self , document):
        raise NotImplementedError
class MultiFunctionPrinter(Machine):
    def print(self,document):
        pass
    def fax(self,document):
        pass
    def scan(self,document):
        pass
class OldFashionedPrinter(Machine):
    def print(self,document):
        pass#ok
    def fax(self,document):
        pass#noop
    def scan(self,document):
        """Not supported!"""
        raise NotImplementedError("Scan not supported")
class Printer:
    @abstractmethod
    def print(self,document):
        print(f'Printing {document}')
class Scanner:
    @abstractmethod
    def scan(self,document):
        print(f'Scanning {document}')
class MyPrinter(Printer):
    def print(self,document):
        print(document)
class Photocopier(Printer,Scanner):
    def print(self,document):
        print(document)
    def scan(self,document):
        print(f'Scanning {document}')
class MultiFunctionDevice(Printer,Scanner):
    @abstractmethod
    def print(self,document):
        pass
    @abstractmethod
    def scan(self,document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self,printer,scanner):
        self.printer=printer
        self.scanner=scanner
    def print(self,document):
        self.printer.print(document)
    def scan(self,document):
        self.scanner.scan(document)
printer=Printer()
scanner=Scanner()
mfm=MultiFunctionMachine(printer,scanner)
mfm.print("Hello World")
mfm.scan("Hello World")