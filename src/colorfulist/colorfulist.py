import colorama
from colorama import Fore
colorama.init()

color_table = {
    'black'  : Fore.BLACK,
    'red'    : Fore.RED,
    'green'  : Fore.GREEN,
    'yellow' : Fore.YELLOW,
    'blue'   : Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan'   : Fore.CYAN,
    'white'  : Fore.WHITE
}

def color2code(color):
    """
    translate color name to console code
    """

    return color_table[color]

class Colors(list):
    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = range(*key.indices(len(self)))
            return [list.__getitem__(self, i) for i in indices]
        return list.__getitem__(self, key)

    def __setitem__(self, key, data):
        #print('before __setitem__:', self, data)
        if isinstance(key, slice):
            if not hasattr(data, '__iter__') or type(data) is str:
                indices = range(*key.indices(len(self )))
                for i in indices:
                    self[i] = data
        else:
            super().__setitem__(key, data)
        #print('after  __setitem__(', key, ',', data, '):', self)

class Colorfulist(list):
    def __init__(self, iterable, print_type='console', default_color = 'white',
                        autocoloring = True):
        """
        @brief Create list from @iterable with field .colors

        example: Colorfulist([1,2,3])

        @param iterable - original list
        @param print_type - 'console' or 'HTML'
        @param default_color - 'white'
        @param autocoloring - True. If True you can use natural color names like
         'red', 'green', 'blue', 'cyan' and etc (see color_table) instead of
          colorama.Fore.RED.
        """
        super().__init__(iterable)
        #print(isinstance(iterable, type(self)), type(iterable), type(super()), type(self))

        self.default_color = default_color
        if isinstance(iterable, type(self)):
            self.colors = Colors(iterable.colors[:])
        else:
            self.colors = Colors([self.default_color for item in iterable])

        self.default_color = default_color
        self.print_type = print_type
        self.autocoloring = autocoloring
        self.set_print_type(print_type, default_color)

    def set_print_type(self, print_type, default_color):
        if print_type == 'console':
            if self.autocoloring:
                def colorize(elem, color):
                    return color2code(color) + str(elem)
                self._colorize = colorize
            else:
                def colorize(elem, color):
                    return color + str(elem)
                self._colorize = colorize


        elif print_type == 'HTML':
            def colorize(elem, color=self.default_color):
                return "<text style=color:{}>{}</text>".format(color, elem)
            self._colorize = colorize

    def coloring(self, function, color):
        for i, elem in enumerate(self):
            if function(elem):
                self.colors[i] = color

    def reset_colors(self):
        for i, elem in enumerate(self.colors):
            self.colors[i] = self.default_color


    def insert(self, index, item):
        super().insert(index, item)
        self.colors.insert(index, self.default_color)

    def append(self, item):
        super().append(item)
        self.colors.append(self.default_color)

    def extend(self, other):
        super().extend(other)
        self.colors.extend([self.default_color for item in other])

    def __str__(self):
        result_str = "["
        result_str += ", ".join([self._colorize(str(item), color) for item, color in zip(self, self.colors)])
        result_str += self._colorize("", self.default_color) + "]"

        return result_str

    def reverse(self):
        super().reverse()
        self.colors.reverse()
