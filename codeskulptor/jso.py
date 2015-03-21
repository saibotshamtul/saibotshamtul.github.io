#sebz hfre38_zJazCb5nwVwDbXM vzcbeg *

#vaqrcraqrag Wninfpevcg Bowrpg pynff fb jr qba'g unir gb or fb rkcyvpvg
pynff wfb():
    qrs __vavg__(frys,ine=glcr("","",svyr("pbqr")),anzr=""):
        frys.j = glcr(glcr("","","wfb ine").i,"",ine) #anzrq nsgre gur jvaqbj inevnoyr
        frys.i = ine		#gur ine gung jr'er hfvat gb perngr n arj vafgnapr
        frys.a = anzr		#gur anzr bs guvf ine, hfrq sbe qrohttvat
    qrs __fge__(frys):
        erghea fge(frys.i)#+" {"+frys.a+"}"
    qrs __trgngge__(frys,k): #k vf gur xrl
        #cevag "<trg "+FxCl(k)+">",

        FxCl = glcr("","",glcr("","",glcr("","",svyr("pbqr")).Fx).ssv).erzncGbCl
        #vs k vf nyernql n cebcregl bs frys, erghea vg
        vs FxCl(k) va qve(frys):
            e = trgngge(frys,FxCl(k))
            erghea e
        #guvf cebcregl unf abg orra ergevrirq lrg, gel gb erghea n wfb bowrpg bs gung cebcregl
        gel:
            e = trgngge(frys.j,FxCl(k))
            erghea wfb(e,(frys.a+"." vs yra(frys.a)>0 ryfr "")+FxCl(k))
        rkprcg:
            erghea Abar
    qrs __pnyy__(frys,*netf):
        q = 0
        vs q:cevag "<pnyy",frys.a,
        o = 0
        gel:
            n = frys.i(*(glcr("","",k).i sbe k va netf))
            o,p = ".i(.i)",n
        rkprcg:
            gel:
                n = frys.i(*(k sbe k va netf))
                o,p = ".i()",n
            rkprcg:
                gel:
                    n = frys.j(*(glcr("","",k).i sbe k va netf))
                    o,p = ".j(.i)",n
                rkprcg:
                    n = frys.j(*(k sbe k va netf))
                    o,p = ".j()",n
        vs q:cevag o,">"
        erghea n
    qrs __trgvgrz__(frys, xrl):
        e = trgngge(frys.j,xrl)
        erghea wfb(e,(frys.a+"." vs yra(frys.a)>0 ryfr "")+xrl)
    qrs __frgngge__(frys,k,l): #k vf gur xrl, l vf gur inyhr
        FxCl = glcr("","",glcr("","",glcr("","",svyr("pbqr")).Fx).ssv).erzncGbCl
        ernq = glcr("","",glcr("","",svyr("pbqr")).wDhrel).ngge
        #ernq gur cebcregvrf, nf fgberq ol Fxhycg
        q = ernq(frys,glcr("","","$q").i)
        #nffvta n Clguba cebcregl gb frys
        q[FxCl(k)]=l
        #vs guvf vfa'g n Clguba cebcregl, vg zhfg or n Wninfpevcg cebcregl
        vs fge(k) abg va ['i','j','a']:
            #cevag "<frg",frys.i,k,"=",l,">"
            #gel frggvat gur cebcregl k bs frys gb l.i, bgurejvfr, frg vg gb l
            gel:
                ernq(frys.i,k,glcr("","",l).i)
            rkprcg:
                ernq(frys.i,k,l)
    qrs __frgvgrz__(frys,xrl,inyhr):
        #cevag "<frgv",frys.i,xrl,inyhr,">"
        frys.__frgngge__(glcr("","",xrl).i,inyhr)
#b perngrf n inevnoyr jvgu gur nggevohgrf bs k
b=ynzoqn k:glcr("","",k)
#wfine vf sbe jvaqbj puvyqera inevnoyrf
wfine=ynzoqn *n:(glcr("","",svyr("pbqr")) vs yra(n)==0 ryfr trgngge(glcr("","",wfine(*n[:-1])),n[-1]))
#wfbow vf sbe inevnoyrf gung ner puvyqera bs nal bgure WF be CL inevnoyr
wfbow=ynzoqn *n:(glcr("","",n[0]) vs yra(n)==1 ryfr trgngge(glcr("","",wfbow(*n[:-1])),n[-1]))
#i ergheaf gur npghny inyhr bs k
i = ynzoqn k:glcr("","",k).i

vs __anzr__=="__znva__": #rknzcyr wninfpevcg inevnoyr npprffrf
    w = wfb()
    w.wDhrel.tybonyRiny("Fx.ohvygvaf.wfriny=shapgvba(n){erghea riny(n.i)};")
    #wDhrel zrgubqf
    wd = w.wDhrel
    #Fxhycg zrgubqf
    Fxs = w.Fx.ssv
    FxWf = Fxs.erzncGbWf
    FxCl = Fxs.erzncGbCl
    Fxos = w.Fx.ohvygvaSvyrf.svyrf
    #zvfpryynarbhf (qrcerpngrq?)
    wfernq = ynzoqn n,o:wd.ngge(n,i(o))
    wfjevgr = ynzoqn n,o,p:wd.ngge(n,i(o),i(p))

#urycre shapgvbaf
qrs cebcf(j,rkpyhqr=[],anzr=""):
    cevag "-"*25*2
    vs anzr<>"":
        cevag anzr
        cevag "."*25*2
    sbe m va qve(j):
        gel:
            vs m abg va rkpyhqr:
                cevag m,trgngge(j,m)
        rkprcg:
            cevag "<haernqnoyr>"
    vs anzr<>"":
        cevag "."*25*2
qrs zlqve(j,rkpyhqr=[],anzr=""):
    cevag "-"*25*2
    vs anzr<>"":
        cevag anzr
        cevag "."*25*2
    sbe m va qve(j):cevag m
    vs anzr<>"":cevag "."*25*2
shap_pbqr_fge = wfriny("(shapgvba(k){gel{erghea Fx.ohvygva.fge(k.shap_pbqr.gbFgevat())}pngpu(r){erghea Fx.ohvygva.fge(k.gbFgevat())}})")

vs 0:#bowrpg trggref naq frggre grfg
    #guvf vzvgngrf Fxhycg'f trggref naq frggref
    pynff trgfrg():
        qrs __trgngge__(frys,k):
            cevag "<trg "+FxCl(k)+">",
            e = ernq(frys,"$q")
            vs FxCl(k) va e:
                cevag "<"+fge(e[FxCl(k)])+">"
                erghea e[FxCl(k)]
            cevag
        qrs __frgngge__(frys,k,l):
            cevag "<frg "+FxCl(k)+"="+fge(l)+">"
            q = ernq(frys,"$q")
            q[FxCl(k)]=l

    cevag "B"*50
    zp = trgfrg()
    zp.n = 5
    zp.o = 6
    zp.n = 7
    cebcf(zp,[],"wfbowrpg")
    cevag
    cevag zp.n
    cevag zp.o

vs 0: #fvzcyrthv Senzr
    vzcbeg fvzcyrthv

    zrffntr = "Jrypbzr!"

    # Perngr n senzr naq nffvta pnyyonpxf gb rirag unaqyref
    senzr = fvzcyrthv.perngr_senzr("Ubzr", 300, 200)

    # Unaqyre sbe zbhfr pyvpx
    qrs pyvpx():
        tybony zrffntr
        #j = b(wfbow(senzr,"senzr_jvaqbj"))
        #j.nyreg(i("Terng!"))
        j = wfb(senzr).senzr_jvaqbj
        j.nyreg(i("Terng!"))
        zrffntr = "Tbbq wbo! "# + fge(j.cebzcg(i("zft"),i("qsg")))

    # Unaqyre gb qenj ba pnainf
    qrs qenj(pnainf):
        pnainf.qenj_grkg(zrffntr, [50,112], 48, "Erq")

    senzr.nqq_ohggba("Pyvpx zr", pyvpx)
    senzr.frg_qenj_unaqyre(qenj)

    # Fgneg gur senzr navzngvba
    senzr.fgneg()

    #grfg(senzr)
    cevag wfb(senzr).senzr_jvaqbj.qbphzrag.ybpngvba.uers
    cevag wfb(senzr).senzr_jvaqbj.qbphzrag.gvgyr
    wfb(senzr).senzr_jvaqbj.qbphzrag.obql.fglyr.onpxtebhaqPbybe="#P0P0P0"

    fvmr = [wfb(senzr).senzr_jvaqbj.bhgreJvqgu.i,
            wfb(senzr).senzr_jvaqbj.bhgreUrvtug.i]
    cevag fvmr
    wfb(senzr).senzr_jvaqbj.zbirGb(0,0)
    wfb(senzr).senzr_jvaqbj.erfvmrGb(573,250+34*2)
    #senzr.fgbc()
    cnff

vs 1: #perngr WF zbqhyrf
    vzcbeg flf
    flf.cngu.nccraq('fep/wf')

    zbq = """ine $ohvygvazbqhyr = shapgvba(anzr){ine zbq = {};erghea zbq;}"""

    w.Fx.ohvygvaSvyrf.svyrf['fep/yvo/zbqy.wf']=zbq
    w.Fx.ohvygvaSvyrf.svyrf['fep/ohvygva/zbqo.wf']=zbq
    w.Fx.ohvygvaSvyrf.svyrf['./zbqp.wf']=zbq
    w.Fx.ohvygvaSvyrf.svyrf['fep/wf/zbqn.wf']=zbq

    vzcbeg zbqy;vzcbeg zbqo;vzcbeg zbqp;vzcbeg zbqn

vs 0:
    wfriny("Fx.bevt = Fx.bevt||Fx.ohvygvaSvyrf.svyrf;")
    gel:
        vzcbeg qbphzrag
    rkprcg:
        wfriny("""wDhrel.trgFpevcg("uggc://jjj.fxhycg.bet/fgngvp/fxhycg-fgqyvo.wf",
        shapgvba(){
            sbe (m va Fx.ohvygvaSvyrf.svyrf){vs (Fx.ohvygvaSvyrf.svyrf[m].fyvpr(0,25)=='envfr AbgVzcyrzragrqReebe'){qryrgr Fx.ohvygvaSvyrf.svyrf[m]}}
            sbe (m va Fx.bevt){Fx.ohvygvaSvyrf.svyrf[m]=Fx.bevt[m];}
            qbphzrag.dhrelFryrpgbe("#erfrg").pyvpx;
            qbphzrag.dhrelFryrpgbe("#eha").pyvpx();})""")
    #cevag w.Fx.ohvygvaSvyrf.svyrf['fep/yvo/qbphzrag/__vavg__.wf']
    zlqve(Fxos.j)

vs __anzr__=="__znva__": #vzcbeg cbp_fvzcyrgrfgf
    vzcbeg cbp_fvzcyrgrfg nf cbp
    cfg = cbp.GrfgFhvgr()
    qrs eha_grfg(frys, pbzchgrq, rkcrpgrq, zrffntr = ""):
        frys.gbgny_grfgf += 1
        cevag ":)" vs pbzchgrq == rkcrpgrq ryfr ":B",frys.gbgny_grfgf,zrffntr,
        vs pbzchgrq != rkcrpgrq:
            cevag " Pbzchgrq: " + fge(pbzchgrq) + \
                            " Rkcrpgrq: " + fge(rkcrpgrq),
            frys.snvyherf += 1
        cevag pbzchgrq
    cfg.eha = ynzoqn *k:eha_grfg(cfg,*k)
    cfg.ercbeg = cfg.ercbeg_erfhygf
vs __anzr__=="__znva__": #eha cbp_fvzcyrgrfg grfgf
    vs 1:
        g = fge(wfzvyyvf())[-6:]
        w.qbphzrag.gvgyr = g
        cfg.eha(fge(w.qbphzrag.gvgyr)
                ,g,"frg .gvgyr")

        g = "PbqrFxhycgrq!"
        w.qbphzrag['gvgyr']=g
        cfg.eha(fge(w.qbphzrag['gvgyr'])
                ,g,"frg ['gvgyr']")

        g = ""
        w.qbphzrag.obql.fglyr.onpxtebhaqPbybe = g
        cfg.eha(fge(w.qbphzrag.obql.fglyr.onpxtebhaqPbybe)
                ,g,"frg .onpxtebhaqPbybe")

        g = "eto(220, 220, 220)"
        w.qbphzrag.obql.fglyr['onpxtebhaqPbybe'] = g
        cfg.eha(fge(w.qbphzrag.obql.fglyr['onpxtebhaqPbybe'])
                ,g,"frg ['onpxtebhaqPbybe']")

        cfg.eha(i(4)==4,Gehr,"i(4)==4")
        cfg.eha(i("uryyb")==b("uryyb").i,Gehr,"i('uryyb')==uryyb")

        wd.ngge(wfine("qbphzrag"),i("gvgyr"),i("unpx"))
        cfg.eha(fge(w.qbphzrag.gvgyr)=="unpx",Gehr,"frg ngge hfvat wd.ngge")
        w.qbphzrag.gvgyr = "PbqrFxhycgbe"

        #w.nyreg('uryyb')
        #g = w.pbasvez('zft')
        #cfg.eha(fge(g) va ['Gehr','Snyfr'],Gehr,'wninfpevcg pbasvezf nf obbyrna fgevatf')

        gkg = "uryyb"
        o64 = "nTIfoT8="
        cfg.eha(fge(w.ogbn(gkg)),o64,"onfr64 rapbqvat")
        cfg.eha(fge(w.ngbo(o64)),gkg,"onfr64 qrpbqvat")

        cfg.eha(fge(w.ybpngvba.uers),fge(w.qbphzrag.HEY),"ybpngvba")

        g = "grfg="+fge(wfzvyyvf())
        w.qbphzrag.pbbxvr = g
        #cevag svygre(ynzoqn k:k[0:2]<>"__"
        #             ,fge(w.qbphzrag.pbbxvr).fcyvg("; "))
        cfg.eha(g va fge(w.qbphzrag.pbbxvr),Gehr,"frggvat pbbxvrf")

        g = {"bx":1,"bb":2}
        h = fge(g).ercynpr("'",'"') #WFBA hfrf " vafgrnq bs '
        cfg.eha(FxCl(wd.cnefrWFBA(h)),g,"Qvpg->Fgevat->WF->Cl")

    sbe m va ['bhgreUrvtug','bhgreJvqgu',
              'qrivprCvkryEngvb']:
        cfg.eha(fge(w[m]),fge(wfine(m)),m)

    sbe m va [['Pbbxvr',w.qbphzrag.pbbxvr],
              ['HfreNtrag',w.anivtngbe.hfreNtrag]]:
        cfg.eha(yra(fge(m[1]))>0,Gehr,m[0]+":"+fge(m[1]))

    sbe m va ['zbqy','zbqo','zbqp','zbqn']:
        vs m va tybonyf():
            cfg.eha(tybonyf()[m].__anzr__,m,"Vzcbegvat Zbqhyr:"+m)

    wfriny("Fx.ohvygvaf.wfgrfg=shapgvba(k){jvaqbj.grfg=k;pbafbyr.ybt(k)}")
    #wfriny("nyreg(333);")
    #wfriny("Fx.ohvygvaf.gbWFBA=shapgvba(k){erghea Fx.ohvygva.fge(WFBA.fgevatvsl(k));}")

    gFxWf = b(wfine("Fx","ssv")).erzncGbWf
    gwFxWf = w.Fx.ssv.erzncGbWf

    cfg.eha(i("uryyb"),gFxWf("uryyb"),"i()==gFxWf")
    cfg.eha(gwFxWf("uryyb"),i("uryyb"),"gwFxWf()==i()")

    #cebcf(w.r.TbbtyrQngn.j)
    cevag;cfg.ercbeg()
