import time

class Shurmark:
    def __init__(self, ser):
        self.ser = ser
        self.linenum = 1
        self.ser.write("$") #to reset slide writer
        self.fontspacing = [22/7.0, 22/11.0, 22/13.0, 22/17.0]

    def line(self, text, fontsize = 2, increment = False):
        self.setfontsize(fontsize)
        if len(text) > int(1/self.fontspacing[self.fontsize-1]*22.0):
            print "too long to fit on slide at current font size"
            print "max chars at font size: " + str(self.fontsize) + " = " + str(int(1/self.fontspacing[self.fontsize-1]*22.0))
        else:
            if self.linenum == 1:
                self.ser.write("#" + str(self.fontsize) + self.lineshift(text)+text)
            else:
                self.ser.write("#N")
                if increment == False:
                    self.ser.write("#" + str(self.fontsize) + self.lineshift(text)+text)
                else:
                    self.ser.write("#" + str(self.fontsize) + self.lineshift(text)+text+"#I")
            self.linenum = self.linenum + 1

    def setfontsize(self, fontsize):
        if fontsize < 1 or fontsize > 4:
            print "Invalid font size, must be between 1 and 4. Defaulting to 2."
            self.fontsize = 2
        else:
            self.fontsize = fontsize
        #self.ser.write("#" + str(self.fontsize))
        
    def dateline(self, fontsize = 2):
        self.setfontsize(fontsize)
        if self.fontsize == 1:
            print "error, font size 1 is too large for date line, changing to font size 2"
            self.changefontsize(2)
        text = time.strftime("%m/%d/%y")
        if self.linenum == 1:
            self.ser.write("#" + str(self.fontsize) + self.lineshift(text)+text)
        else:
            self.ser.write("#N")
            self.ser.write("#" + str(self.fontsize) + self.lineshift(text)+text)
        self.linenum = self.linenum + 1

    def lineshift(self, text):
        lineshift = (22-len(text)*self.fontspacing[self.fontsize-1])/2.0*10.0
        lineshift = str(int(round(lineshift)))
        if len(lineshift) == 1:
            lineshift = "0" + lineshift
        lineshift = "#R" + lineshift
        return lineshift

    def writeslide(self, numslides = 1):
        if numslides > 99 or numslides < 1:
            print "number of slides must be between 1 and 99, prining 1 slide instead"
        if numslides != 1:
            self.ser.write("#G"+str(numslides))
        self.ser.write("\r\n")
        self.linenum = 1
