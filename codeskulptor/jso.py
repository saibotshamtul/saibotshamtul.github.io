#from user38_mWnmPo5ajIjQoKZ import *

#independent Javascript Object class so we don't have to be so explicit
class jso():
    def __init__(self,var=type("","",file("code")),name=""):
        self.w = type(type("","","jso var").v,"",var) #named after the window variable
        self.v = var		#the var that we're using to create a new instance
        self.n = name		#the name of this var, used for debugging
    def __str__(self):
        return str(self.v)#+" {"+self.n+"}"
    def __getattr__(self,x): #x is the key
        #print "<get "+SkPy(x)+">",

        SkPy = type("","",type("","",type("","",file("code")).Sk).ffi).remapToPy
        #if x is already a property of self, return it
        if SkPy(x) in dir(self):
            r = getattr(self,SkPy(x))
            return r
        #this property has not been retrieved yet, try to return a jso object of that property
        try:
            r = getattr(self.w,SkPy(x))
            return jso(r,(self.n+"." if len(self.n)>0 else "")+SkPy(x))
        except:
            return None
    def __call__(self,*args):
        d = 0
        if d:print "<call",self.n,
        b = 0
        try:
            a = self.v(*(type("","",x).v for x in args))
            b,c = ".v(.v)",a
        except:
            try:
                a = self.v(*(x for x in args))
                b,c = ".v()",a
            except:
                try:
                    a = self.w(*(type("","",x).v for x in args))
                    b,c = ".w(.v)",a
                except:
                    a = self.w(*(x for x in args))
                    b,c = ".w()",a
        if d:print b,">"
        return a
    def __getitem__(self, key):
        r = getattr(self.w,key)
        return jso(r,(self.n+"." if len(self.n)>0 else "")+key)
    def __setattr__(self,x,y): #x is the key, y is the value
        SkPy = type("","",type("","",type("","",file("code")).Sk).ffi).remapToPy
        read = type("","",type("","",file("code")).jQuery).attr
        #read the properties, as stored by Skulpt
        d = read(self,type("","","$d").v)
        #assign a Python property to self
        d[SkPy(x)]=y
        #if this isn't a Python property, it must be a Javascript property
        if str(x) not in ['v','w','n']:
            #print "<set",self.v,x,"=",y,">"
            #try setting the property x of self to y.v, otherwise, set it to y
            try:
                read(self.v,x,type("","",y).v)
            except:
                read(self.v,x,y)
    def __setitem__(self,key,value):
        #print "<seti",self.v,key,value,">"
        self.__setattr__(type("","",key).v,value)
#o creates a variable with the attributes of x
o=lambda x:type("","",x)
#jsvar is for window children variables
jsvar=lambda *a:(type("","",file("code")) if len(a)==0 else getattr(type("","",jsvar(*a[:-1])),a[-1]))
#jsobj is for variables that are children of any other JS or PY variable
jsobj=lambda *a:(type("","",a[0]) if len(a)==1 else getattr(type("","",jsobj(*a[:-1])),a[-1]))
#v returns the actual value of x
v = lambda x:type("","",x).v

if __name__=="__main__": #example javascript variable accesses
    j = jso()
    j.jQuery.globalEval("Sk.builtins.jseval=function(a){return eval(a.v)};")
    #jQuery methods
    jq = j.jQuery
    #Skulpt methods
    Skf = j.Sk.ffi
    SkJs = Skf.remapToJs
    SkPy = Skf.remapToPy
    Skbf = j.Sk.builtinFiles.files
    #miscellaneous (deprecated?)
    jsread = lambda a,b:jq.attr(a,v(b))
    jswrite = lambda a,b,c:jq.attr(a,v(b),v(c))

#helper functions
def props(w,exclude=[],name=""):
    print "-"*25*2
    if name<>"":
        print name
        print "."*25*2
    for z in dir(w):
        try:
            if z not in exclude:
                print z,getattr(w,z)
        except:
            print "<unreadable>"
    if name<>"":
        print "."*25*2
def mydir(w,exclude=[],name=""):
    print "-"*25*2
    if name<>"":
        print name
        print "."*25*2
    for z in dir(w):print z
    if name<>"":print "."*25*2
func_code_str = jseval("(function(x){try{return Sk.builtin.str(x.func_code.toString())}catch(e){return Sk.builtin.str(x.toString())}})")

if 0:#object getters and setter test
    #this imitates Skulpt's getters and setters
    class getset():
        def __getattr__(self,x):
            print "<get "+SkPy(x)+">",
            r = read(self,"$d")
            if SkPy(x) in r:
                print "<"+str(r[SkPy(x)])+">"
                return r[SkPy(x)]
            print
        def __setattr__(self,x,y):
            print "<set "+SkPy(x)+"="+str(y)+">"
            d = read(self,"$d")
            d[SkPy(x)]=y

    print "O"*50
    mc = getset()
    mc.a = 5
    mc.b = 6
    mc.a = 7
    props(mc,[],"jsobject")
    print
    print mc.a
    print mc.b

if 0: #simplegui Frame
    import simplegui

    message = "Welcome!"

    # Create a frame and assign callbacks to event handlers
    frame = simplegui.create_frame("Home", 300, 200)

    # Handler for mouse click
    def click():
        global message
        #w = o(jsobj(frame,"frame_window"))
        #w.alert(v("Great!"))
        w = jso(frame).frame_window
        w.alert(v("Great!"))
        message = "Good job! "# + str(w.prompt(v("msg"),v("dft")))

    # Handler to draw on canvas
    def draw(canvas):
        canvas.draw_text(message, [50,112], 48, "Red")

    frame.add_button("Click me", click)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()

    #test(frame)
    print jso(frame).frame_window.document.location.href
    print jso(frame).frame_window.document.title
    jso(frame).frame_window.document.body.style.backgroundColor="#C0C0C0"

    size = [jso(frame).frame_window.outerWidth.v,
            jso(frame).frame_window.outerHeight.v]
    print size
    jso(frame).frame_window.moveTo(0,0)
    jso(frame).frame_window.resizeTo(573,250+34*2)
    #frame.stop()
    pass

if 1: #create JS modules
    import sys
    sys.path.append('src/js')

    mod = """var $builtinmodule = function(name){var mod = {};return mod;}"""

    j.Sk.builtinFiles.files['src/lib/modl.js']=mod
    j.Sk.builtinFiles.files['src/builtin/modb.js']=mod
    j.Sk.builtinFiles.files['./modc.js']=mod
    j.Sk.builtinFiles.files['src/js/moda.js']=mod

    import modl;import modb;import modc;import moda

if 0:
    jseval("Sk.orig = Sk.orig||Sk.builtinFiles.files;")
    try:
        import document
    except:
        jseval("""jQuery.getScript("http://www.skulpt.org/static/skulpt-stdlib.js",
        function(){
            for (z in Sk.builtinFiles.files){if (Sk.builtinFiles.files[z].slice(0,25)=='raise NotImplementedError'){delete Sk.builtinFiles.files[z]}}
            for (z in Sk.orig){Sk.builtinFiles.files[z]=Sk.orig[z];}
            document.querySelector("#reset").click;
            document.querySelector("#run").click();})""")
    #print j.Sk.builtinFiles.files['src/lib/document/__init__.js']
    mydir(Skbf.w)

if __name__=="__main__": #import poc_simpletests
    import poc_simpletest as poc
    pst = poc.TestSuite()
    def run_test(self, computed, expected, message = ""):
        self.total_tests += 1
        print ":)" if computed == expected else ":O",self.total_tests,message,
        if computed != expected:
            print " Computed: " + str(computed) + \
                            " Expected: " + str(expected),
            self.failures += 1
        print computed
    pst.run = lambda *x:run_test(pst,*x)
    pst.report = pst.report_results
if __name__=="__main__": #run poc_simpletest tests
    if 1:
        t = str(jsmillis())[-6:]
        j.document.title = t
        pst.run(str(j.document.title)
                ,t,"set .title")

        t = "CodeSkulpted!"
        j.document['title']=t
        pst.run(str(j.document['title'])
                ,t,"set ['title']")

        t = ""
        j.document.body.style.backgroundColor = t
        pst.run(str(j.document.body.style.backgroundColor)
                ,t,"set .backgroundColor")

        t = "rgb(220, 220, 220)"
        j.document.body.style['backgroundColor'] = t
        pst.run(str(j.document.body.style['backgroundColor'])
                ,t,"set ['backgroundColor']")

        pst.run(v(4)==4,True,"v(4)==4")
        pst.run(v("hello")==o("hello").v,True,"v('hello')==hello")

        jq.attr(jsvar("document"),v("title"),v("hack"))
        pst.run(str(j.document.title)=="hack",True,"set attr using jq.attr")
        j.document.title = "CodeSkulptor"

        #j.alert('hello')
        #t = j.confirm('msg')
        #pst.run(str(t) in ['True','False'],True,'javascript confirms as boolean strings')

        txt = "hello"
        b64 = "aGVsbG8="
        pst.run(str(j.btoa(txt)),b64,"base64 encoding")
        pst.run(str(j.atob(b64)),txt,"base64 decoding")

        pst.run(str(j.location.href),str(j.document.URL),"location")

        t = "test="+str(jsmillis())
        j.document.cookie = t
        #print filter(lambda x:x[0:2]<>"__"
        #             ,str(j.document.cookie).split("; "))
        pst.run(t in str(j.document.cookie),True,"setting cookies")

        t = {"ok":1,"oo":2}
        u = str(t).replace("'",'"') #JSON uses " instead of '
        pst.run(SkPy(jq.parseJSON(u)),t,"Dict->String->JS->Py")

    for z in ['outerHeight','outerWidth',
              'devicePixelRatio']:
        pst.run(str(j[z]),str(jsvar(z)),z)

    for z in [['Cookie',j.document.cookie],
              ['UserAgent',j.navigator.userAgent]]:
        pst.run(len(str(z[1]))>0,True,z[0]+":"+str(z[1]))

    for z in ['modl','modb','modc','moda']:
        if z in globals():
            pst.run(globals()[z].__name__,z,"Importing Module:"+z)

    jseval("Sk.builtins.jstest=function(x){window.test=x;console.log(x)}")
    #jseval("alert(333);")
    #jseval("Sk.builtins.toJSON=function(x){return Sk.builtin.str(JSON.stringify(x));}")

    tSkJs = o(jsvar("Sk","ffi")).remapToJs
    tjSkJs = j.Sk.ffi.remapToJs

    pst.run(v("hello"),tSkJs("hello"),"v()==tSkJs")
    pst.run(tjSkJs("hello"),v("hello"),"tjSkJs()==v()")

    #props(j.e.GoogleData.w)
    print;pst.report()