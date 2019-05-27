import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from ui import MainWindow, CalibDialog, CalibDialog1,SizeDialog

import cv2
import numpy as np
import time
import imutils
from scipy.spatial import distance as dist
from imutils import perspective
import json
from numpy import mintypecode
from imutils.video.videostream import VideoStream
import os
import RPi.GPIO as GPIO
from matplotlib import pyplot as plt



stop = True
name = None
mint = None
maxt = None

class wizard1(CalibDialog1.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(wizard1,self).__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.inicio)
        self.next.clicked.connect(self.fin)
        
    def fin(self):
        global name
        global mint 
        global maxt
        global size
        x = {
            "name": name,
            "size": size,
            "minimum": mint,
            "maximum": maxt
            }
        with open(str(name) + '.json', 'w+') as outfile: #a para append, w+ para crear si no existe
            json.dump(x, outfile)
        
        
        
        self.close()
        #y = json.dumps(x)
        #print(y)

    
    def inicio(self):
        x=0
        #print("hola")

        
        def servo():
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(11,GPIO.OUT)
            p = GPIO.PWM(11,50)
            p.start(0)
            p.ChangeDutyCycle(12)
            time.sleep(0.25)
            p.stop()
            time.sleep(0.75)
            p.start(0)
            p.ChangeDutyCycle(3)
            time.sleep(0.25)
            GPIO.cleanup()
            
        def detect(img):
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            low_up = np.array([0, 90, 0])
            upper = np.array([255, 255, 255])
            mask = cv2.inRange(img_hsv, low_up, upper)
            src = cv2.medianBlur(mask, 15)
            src2=cv2.medianBlur(src,15)
            res = cv2.bitwise_and(img, img, mask=src2)
            edged = cv2.Canny(src2, 100, 200)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            i=0
            for c in cnts:
                if cv2.contourArea(c) < 10000:
                    continue
                i=i+1
            return i, res
            
        def histo(res):
            gra = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
            hist = cv2.calcHist([gra], [0], None, [180], [1, 180])
            (_,_,_,maxv)=cv2.minMaxLoc(hist)
            return maxv[1]
        

        hist1=[0,0,0,0,0]
        hist0=[0,0,0,0,0]
        
        cap0 = VideoStream(src=0).start()
        cap1 = VideoStream(src=1).start()
        while True:
            
            while True:
                img0 = cap0.read()
                img1 = cap1.read()
                
                n0, hsv0 = detect(img0)
                n1, hsv1 = detect(img1)
                if n0 == 1 and n1 == 1:
                    break
            hist0[x] = histo(hsv0)
            hist1[x] = histo(hsv1)
            servo()
            x=x+1
            self.falta.setText(str(5-x))
            if (x == 5):
                break
        print(hist0)
        print(hist1)
        cap0.stop()
        cap1.stop()
        cap0 = None
        cap1 = None
        
        min0 = min(hist0)
        max0 = max(hist0)
        min1 = min(hist1)
        max1 = max(hist1)
        global mint
        global maxt
        mint = min(min0,min1)
        maxt = max(max0, max1)
        self.falta.setText("Listo")
        
        
        

        
class wizard0(CalibDialog.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(wizard0,self).__init__()
        self.setupUi(self)
        
        self.next.clicked.connect(self.open1)
        
        #t = MainWindow.Ui_mainWindow.select.currentText()
        


        
    def open1(self):
        text = self.fruit_name.toPlainText()
        global name
        name = text
        self.close()
        global size
        if (self.p.isChecked() == True):
            size = "small"
        if (self.m.isChecked() == True):
            size = "medium"
        if (self.g.isChecked() == True):
            size = "big"
        
        widget1 = wizard1()
        widget1.exec_()

class size0(SizeDialog.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(size0,self).__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.inicio)
        self.next.clicked.connect(self.fin)


    def inicio(self):   

        cap0 = VideoStream(src=0).start()
        cap1 = VideoStream(src=1).start()
        n0=0
        n1=0
        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5) 

        def detect(sel,cm):
           
            while (True):
                if (sel==0):
                    img = cap0.read()
                elif (sel==1):
                    img = cap1.read()
                ppmA=0
                ppmB=0
                img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                low_up = np.array([0, 90, 0])
                upper = np.array([255, 255, 255])
                mask = cv2.inRange(img_hsv, low_up, upper)
                src = cv2.medianBlur(mask, 15)
                src2=cv2.medianBlur(src,15)
                edged = cv2.Canny(src2, 100, 200)
                edged = cv2.dilate(edged, None, iterations=1)
                edged = cv2.erode(edged, None, iterations=1)
                cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                i=0
                for c in cnts:
                    if cv2.contourArea(c) < 10000:
                        continue
                    i=i+1
                if i == 1:
                    break
                
            
            
            for c in cnts:
                if cv2.contourArea(c) < 10000:
                    continue
                
                box = cv2.minAreaRect(c)
                box = cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                box = perspective.order_points(box)
                cv2.drawContours(img, [box.astype("int")], -1, (0, 255, 0), 2)
                for (x, y) in box:
                    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)
                cv2.circle(img, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
                cv2.circle(img, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
                cv2.circle(img, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
                cv2.circle(img, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
                cv2.line(img, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
                cv2.line(img, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                ppmA = dA / cm
                ppmB = dB / cm
                
            return ppmA, ppmB, i
        
        def servo():
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(11,GPIO.OUT)
            p = GPIO.PWM(11,50)
            p.start(0)
            p.ChangeDutyCycle(12)
            time.sleep(0.25)
            p.stop()
            time.sleep(0.75)
            p.start(0)
            p.ChangeDutyCycle(3)
            time.sleep(0.25)
            GPIO.cleanup()
        
        while (True):
            PA0, PB0, n0 = detect(0,3.93)
            PA1, PB1, n1 = detect(1, 3.93)
            if n0 == 1 and n1 == 1:
                servo()
                break
        print(PA0,PB0)
        print(PA1,PB1)
        self.p.setText("Listo")
        n0=0
        n1=0
        while (True):
            MA0, MB0, n0 = detect(0,7.87)
            MA1, MB1, n1 = detect(1, 7.87)
            if n0 == 1 and n1 == 1:
                servo()
                break
        print(MA0,MB0)
        print(MA1,MB1)
        self.m.setText("Listo")


        
        x = {
            "PA0": PA0,
            "PB0": PB0,
            "PA1": PA1,
            "PB1": PB1,
            "MA0": MA0,
            "MB0": MB0,
            "MA1": MA1,
            "MB1": MB1
            }
        
        with open('tamano.json', 'w+') as outfile:
            json.dump(x, outfile)
        
        cap0.stop()
        cap1.stop()
        cap0 = None
        cap1 = None     

        
    def fin(self):
        self.close()

class MyQtApp(MainWindow.Ui_mainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        
        self.captura.clicked.connect(self.inic)
        self.stop.clicked.connect(self.stopp)
        self.new_2.clicked.connect(self.open0)
        self.calib.clicked.connect(self.open_calib)

        cwd = os.getcwd()       
        for file in os.listdir(cwd):
            if file.endswith(".json"):
                name, ext = os.path.splitext(file)
                if (name != 'tamano'):
                    #print(name)
                    self.select.addItem(name)
                    

    def updatee(self):
        self.select.addItem("holi")
        
    def open_calib(self):
        widget = size0()
        widget.exec_()
    
    def open0(self):
        widget0 = wizard0()
        widget0.exec_()
    
    
    def inic(self):
        
        def histo(image):
            gra = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            hist = cv2.calcHist([gra], [0], None, [180], [1, 180])
            #plt.clf()
            #plt.plot(hist,color='k')
            #plt.show()
            (_,_,_,maxv)=cv2.minMaxLoc(hist)
            return maxv[1]
        
        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5) 

        def detect(img):
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            low_up = np.array([0, 90, 0])
            upper = np.array([255, 255, 255])
            mask = cv2.inRange(img_hsv, low_up, upper)
            src = cv2.medianBlur(mask, 15)
            src2=cv2.medianBlur(src,15)
            res = cv2.bitwise_and(img, img, mask=src2)
            edged = cv2.Canny(src2, 100, 200)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            i=0
            for c in cnts:
                if cv2.contourArea(c) < 10000:
                    continue
                i=i+1
            return i, res, cnts
          
        def prueba(orig, cnts, PMA, PMB):
                for c in cnts:
                    if cv2.contourArea(c) < 5000:
                        continue
                    box = cv2.minAreaRect(c)
                    box = cv2.boxPoints(box)
                    box = np.array(box, dtype="int")
                    box = perspective.order_points(box)
                    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
                    for (x, y) in box:
                        cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
                    (tl, tr, br, bl) = box
                    (tltrX, tltrY) = midpoint(tl, tr)
                    (blbrX, blbrY) = midpoint(bl, br)
                    (tlblX, tlblY) = midpoint(tl, bl)
                    (trbrX, trbrY) = midpoint(tr, br)
                    cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
                    cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
                    cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
                    cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
                    cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
                    cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
                    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                    dimA = dA / PMA
                    dimB = dB / PMB
                    cv2.putText(orig, "{:.2f}cm".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                                0.65, (255, 255, 255), 2)
                    cv2.putText(orig, "{:.2f}cm".format(dimB), (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                                0.65, (255, 255, 255), 2)
                #self.display.show()
                return orig
            
        def show(orig):
                img = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
                self.img = QtGui.QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
                self.pix = QtGui.QPixmap(self.img)
                self.display.setPixmap(self.pix)
        
        def calibra(img):
            dist = np.array([[-0.38536548, 2.94095511, -0.02413613, -0.00698944, -6.88773824]], dtype='float')

            mtx = np.array([[1.00212662e+03, 0.00000000e+00, 2.87534946e+02],
                            [0.00000000e+00, 1.08701122e+03, 6.99760058e+01],
                            [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]], dtype='float')

            rvecs = np.array([[[0.39958429], [-0.03999056], [0.61024387]]], dtype='float')
            tvecs = np.array([[-1.28578658], [0.08522974], [21.03160133]], dtype='float')
            h, w = img.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
            mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
            dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
            x, y, w, h = roi
            dst = dst[y:y + h, x:x + w]
            return dst        
        
        
        global cap0
        global cap1
        global stop
        global mini
        global maxi
        global A0
        global B0
        global A1
        global B1
        #print(stop)
        if stop == True:
            t = self.select.currentText()
            with open(str(t) +'.json', 'r') as myfile:
                data=myfile.read()
            obj = json.loads(data)
            print(str(obj['name']))
            mini = obj['minimum']
            print(mini)
            maxi = obj['maximum']
            print(maxi)
            tama = obj['size']
            if str(tama) == 'small':
                with open('tamano.json', 'r') as myfile:
                    data=myfile.read()
                obj = json.loads(data)
                A0 = obj['PA0']
                B0 = obj['PB0']
                A1 = obj['PA1']
                B1 = obj['PB1']
                #print(A0,B0)
                
            if str(tama) == 'medium':
                with open('tamano.json', 'r') as myfile:
                    data=myfile.read()
                obj = json.loads(data)
                A0 = obj['MA0']
                B0 = obj['MB0']
                A1 = obj['MA1']
                B1 = obj['MB1']
               #print(A0,B0)
                 
            
            
            
            cap0 = VideoStream(src=0)
            cap0.start()
            cap1 = VideoStream(src=1)
            cap1.start()
        stop = False
        while (True):
            img0 = cap0.read()
            img1 = cap1.read()
            
                       
            n0, hsv0, cnts0 = detect(img0)
            n1, hsv1, cnts1 = detect(img1)
            #print(n0)
            #cv2.imshow("a",hsv0)
            #cv2.imshow("b",hsv1)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if n0 == 1 and n1 == 1:
                time.sleep(0.5)
                img0 = cap0.read()
                img1 = cap1.read()           
                n0, hsv0, cnts0 = detect(img0)
                n1, hsv1, cnts1 = detect(img1)
                break
        self.servo()
        hist0 = histo(hsv0)
        hist1 = histo(hsv1)
            
        if (hist0 >= mini and hist0 <= maxi):
        #if (hist0 > 0 and hist0 < 200):
            camara0 = prueba(img0, cnts0, A0, B0)
            camara1 = prueba(img1, cnts1, A1, B1)
            show(camara0) 

        self.checkk()
    def stopp(self):
        global stop
        global cap0
        global cap1
        stop = True
        cap0.stop()
        cap0=None
        cap1.stop()
        cap1=None

    def checkk(self):
        if(stop == False):
            self.inic()
    
    def servo(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        p = GPIO.PWM(11,50)
        p.start(0)
        p.ChangeDutyCycle(12)
        time.sleep(0.25)
        p.stop()
        time.sleep(0.75)
        p.start(0)
        p.ChangeDutyCycle(3)
        time.sleep(0.25)
        GPIO.cleanup()
   
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
