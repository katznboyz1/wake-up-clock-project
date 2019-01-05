import os as os
import pygame as pygame
import time as time
import h_clocklib as clocklib
import datetime as datetime
 
class pyscope :
    screen = None
    running = True
    data = {}
    blinkstate = True
    def __init__(self):
        os.system("""gpio -g mode 18 pwm""")
        os.system("""gpio pwmc 1000""")
        os.system("""sudo sh -c 'echo "0" > /sys/class/backlight/soc\:backlight/brightness'""")
        os.putenv('SDL_VIDEODRIVER', 'fbcon')
        os.putenv('SDL_FBDEV', '/dev/fb1')
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print ("I'm running under X display = {0}".format(disp_no))
        drivers = ['fbcon', 'directfb', 'svgalib']
        try:
            pygame.display.init()
            found = True
        except:
            found = False
        if (found != True):
            for driver in drivers:
                if not os.getenv('SDL_VIDEODRIVER'):
                    os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    print ('Driver: {0} failed.'.format(driver))
                    continue
                found = True
                break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print ("Framebuffer size: %d x %d" % (size[0], size[1]))
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.screen.fill((0, 0, 0))        
        pygame.font.init()
        pygame.display.update()

        pygame.mouse.set_visible(False)
 
    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."
    
    def text(self, fontFace, size, text, color):
        font = pygame.font.Font(fontFace, size)
        text = font.render(text, 1, color)
        return text
 
    def test(self):
        while (self.running):
            exec('self.data = {}'.format(str(open('./h_data/data.txt').read())))
            timenow = clocklib.timeget.getSecondsSinceMidnight()
            weekday = datetime.date.today().strftime("%A").lower()
            wakeuptime = int(self.data['wakeUpTimes'][weekday])
            wakeuptimelimit = int(self.data['wakeUpLengths'][weekday])
            bgcolor = self.data['backgroundColor']
            fgcolor = self.data['foregroundColor']
            if (timenow > wakeuptime and timenow < (wakeuptime + wakeuptimelimit)): #changes the color of the background and foreground if it is time to wake up
                bgcolor = self.data['wakeUpBackgroundColor']
                fgcolor = self.data['wakeUpForegroundColor']
            try:
                self.screen.fill(bgcolor)
            except:
                self.screen.fill((0, 0, 0))
            try:
                t = self.text('./h_fonts/digital.TTF', int(self.data['fontSize']), (clocklib.timeget.getDisplayableTime() if self.blinkstate else clocklib.timeget.getDisplayableTime().replace(':', ' ')), fgcolor)
                d = self.text('./h_fonts/digital.TTF', int(self.data['dateFontSize']), weekday.upper(), fgcolor)
            except:
                t = self.text('./h_fonts/digital.TTF', 20, (clocklib.timeget.getDisplayableTime() if self.blinkstate else clocklib.timeget.getDisplayableTime().replace(':', ' ')), (255, 255, 255))
                d = self.text('./h_fonts/digital.TTF', 20, weekday.upper(), (255, 255, 255))
            y1 = self.screen.get_size()[1]
            xtra = y1 - t.get_size()[1]
            y1 = xtra / 2
            y1 -= d.get_size()[1] / 2
            x1 = self.screen.get_size()[0]
            xtra = x1 - t.get_size()[0]
            x1 = xtra / 2
            y2 = y1 + t.get_size()[1]
            x2 = (self.screen.get_size()[0] - d.get_size()[0]) / 2
            self.screen.blit(t, (x1, y1))
            self.screen.blit(d, (x2, y2))
            pygame.display.update()
            if (int(self.data['screenBrightness']) >= 0 and int(self.data['screenBrightness']) <= 1000):
                os.system('gpio -g pwm 18 {}'.format(self.data['screenBrightness']))
            blinkstate = True #toggles if the : is visible in the time
            time.sleep(1)
 
scope = pyscope()
scope.test()
