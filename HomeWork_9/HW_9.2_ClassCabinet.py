class Cabinet:
    top = None
    middle = None
    bottom = None

    def SetPropr(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom

    def PutOn(self, shelf, thing):
        name = ["top", "middle", "bottom"]
        self.shelfname = [self.top, self.middle, self.bottom]
        i = name.index(shelf)
        if self.shelfname[i] is None:
            if i == 0:
                self.top = thing
            elif i == 1:
                self.middle = thing
            else:
                self.bottom = thing
            print(f'You put {thing} on {name[i]} shel')
        else:
            print(f'Cannot place {thing} on {shelf} shelf, it is not empty!')

    def TakeFrom(self, shelf):
        name = ["top", "middle", "bottom"]
        self.shelfname = [self.top, self.middle, self.bottom]
        i = name.index(shelf)
        if self.shelfname[i] is not None:
            if i == 0:
                print(f'You take {self.top} from {shelf} shelf')
                self.top = None
            elif i == 1:
                print(f'You take {self.middle} from {shelf} shelf')
                self.middle = None
            else:
                print(f'You take {self.bottom} from {shelf} shelf')
                self.bottom = None
        else:
            print(f'Nothing to take! The {shelf} shelf is empty')

    def PrintSchema(self):
        print("=" * 31)
        try:
            print(f'# {self.top:^28s}#\n', "=" * 31, sep="")
        except:
            print('#', " " * 29, "#\n", "=" * 31, sep="")
        try:
            print(f'# {self.middle:^28s}#\n', "=" * 31, sep="")
        except:
            print('#', " " * 29, "#\n", "=" * 31, sep="")
        try:
            print(f'# {self.bottom:^28s}#\n', "=" * 31, sep="")
        except:
            print('#', " " * 29, "#\n", "=" * 31, sep="")


d1 = Cabinet()
d1.SetPropr("flash light", "apple", "book")
d1.TakeFrom("middle")
d1.PutOn("middle", "phone")
d1.TakeFrom("top")
d1.PrintSchema()
