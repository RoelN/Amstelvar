from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
import os

designSpacePath = "AmstelvarAlpha.designspace"
familyName = "AmstelvarAlpha"

sources = [
	dict(path="master_ufo/AmstelvarAlpha-Default.ufo", name="AmstelvarAlpha-Default.ufo", location=dict(weight=400, width=100, opticalsize=14, xopaque=88, xtransparent=402, yopaque=50, lcytransparent=500, serifheight=18, grade=88, xtransch=1000, ytransch=1000, ytransas=750, ytransde=250, ytransuc=750, ytransparent=1000, paraweight=88, parawidth=402), styleName="Default", familyName=familyName, copyInfo=True),
	# registered
	dict(path="master_ufo/AmstelvarAlpha-wght-min.ufo", name="AmstelvarAlpha-wght-min.ufo", location=dict(weight=100), styleName="wght-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-wght-max.ufo", name="AmstelvarAlpha-wght-max.ufo", location=dict(weight=900), styleName="wght-max", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-wght-min.ufo", name="AmstelvarAlpha-wght-min.ufo", location=dict(paraweight=38), styleName="wght-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-wght-max.ufo", name="AmstelvarAlpha-wght-max.ufo", location=dict(paraweight=250), styleName="wght-max", familyName=familyName, copyInfo=False),
	
	dict(path="master_ufo/AmstelvarAlpha-wdth-min.ufo", name="AmstelvarAlpha-wdth-min.ufo", location=dict(width=35), styleName="wdth-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-wdth-min.ufo", name="AmstelvarAlpha-wdth-min.ufo", location=dict(parawidth=60), styleName="wdth-min", familyName=familyName, copyInfo=False),
	##dict(path="master_ufo/AmstelvarAlpha-wdth-151.ufo", name="AmstelvarAlpha-wdth-151.ufo", location=dict(width=151.999), styleName="wdth-151", familyName=familyName, copyInfo=False),
	##dict(path="master_ufo/AmstelvarAlpha-wdth-152.ufo", name="AmstelvarAlpha-wdth-152.ufo", location=dict(width=152), styleName="wdth-152", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/AmstelvarAlpha-opsz-min.ufo", name="AmstelvarAlpha-opsz-min.ufo", location=dict(opticalsize=10), styleName="opsz-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-opsz-max.ufo", name="AmstelvarAlpha-opsz-max.ufo", location=dict(opticalsize=72), styleName="opsz-max", familyName=familyName, copyInfo=False),

	# private
	dict(path="master_ufo/AmstelvarAlpha-XOPQ-min.ufo", name="AmstelvarAlpha-XOPQ-min.ufo", location=dict(xopaque=5), styleName="XOPQ-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-XOPQ-max.ufo", name="AmstelvarAlpha-XOPQ-max.ufo", location=dict(xopaque=500), styleName="XOPQ-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/AmstelvarAlpha-XTRA-min.ufo", name="AmstelvarAlpha-XTRA-min.ufo", location=dict(xtransparent=42), styleName="XTRA-min", familyName=familyName, copyInfo=False),
	##dict(path="master_ufo/AmstelvarAlpha-XTRA-151.ufo", name="AmstelvarAlpha-XTRA-151.ufo", location=dict(xtransparent=151.999), styleName="XTRA-151", familyName=familyName, copyInfo=False),
	##dict(path="master_ufo/AmstelvarAlpha-XTRA-152.ufo", name="AmstelvarAlpha-XTRA-152.ufo", location=dict(xtransparent=152), styleName="XTRA-152", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/AmstelvarAlpha-YOPQ-min.ufo", name="AmstelvarAlpha-YOPQ-min.ufo", location=dict(yopaque=4), styleName="YOPQ-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YOPQ-max.ufo", name="AmstelvarAlpha-YOPQ-max.ufo", location=dict(yopaque=85), styleName="YOPQ-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/AmstelvarAlpha-YTLC-min.ufo", name="AmstelvarAlpha-YTLC-min.ufo", location=dict(lcytransparent=445), styleName="YTLC-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTLC-max.ufo", name="AmstelvarAlpha-YTLC-max.ufo", location=dict(lcytransparent=600), styleName="YTLC-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/AmstelvarAlpha-YTSE-min.ufo", name="AmstelvarAlpha-YTSE-min.ufo", location=dict(serifheight=0), styleName="YTSE-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTSE-max.ufo", name="AmstelvarAlpha-YTSE-max.ufo", location=dict(serifheight=48), styleName="YTSE-max", familyName=familyName, copyInfo=False),
	
	#dict(path="master_ufo/AmstelvarAlpha-GRAD-min.ufo", name="AmstelvarAlpha-GRAD-min.ufo", location=dict(grade=25), styleName="GRAD-min", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/AmstelvarAlpha-GRAD-max.ufo", name="AmstelvarAlpha-GRAD-max.ufo", location=dict(grade=250), styleName="GRAD-max", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-GRAD-max.ufo", name="AmstelvarAlpha-GRAD-max.ufo", location=dict(grade=150), styleName="GRAD-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/AmstelvarAlpha-XTCH-min.ufo", name="AmstelvarAlpha-XTCH-min.ufo", location=dict(xtransch=800), styleName="XTCH-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-XTCH-max.ufo", name="AmstelvarAlpha-XTCH-max.ufo", location=dict(xtransch=1200), styleName="XTCH-max", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTCH-min.ufo", name="AmstelvarAlpha-YTCH-min.ufo", location=dict(ytransch=800), styleName="YTCH-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTCH-max.ufo", name="AmstelvarAlpha-YTCH-max.ufo", location=dict(ytransch=1200), styleName="YTCH-max", familyName=familyName, copyInfo=False),
	
	dict(path="master_ufo/AmstelvarAlpha-YTAS-min.ufo", name="AmstelvarAlpha-YTAS-min.ufo", location=dict(ytransas=650), styleName="YTAS-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTAS-max.ufo", name="AmstelvarAlpha-YTAS-max.ufo", location=dict(ytransas=850), styleName="YTAS-max", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTDE-min.ufo", name="AmstelvarAlpha-YTDE-min.ufo", location=dict(ytransde=150), styleName="YTDE-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTDE-max.ufo", name="AmstelvarAlpha-YTDE-max.ufo", location=dict(ytransde=350), styleName="YTDE-max", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTUC-min.ufo", name="AmstelvarAlpha-YTUC-min.ufo", location=dict(ytransuc=650), styleName="YTUC-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTUC-max.ufo", name="AmstelvarAlpha-YTUC-max.ufo", location=dict(ytransuc=950), styleName="YTUC-max", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTRA-min.ufo", name="AmstelvarAlpha-YTRA-min.ufo", location=dict(ytransparent=800), styleName="YTRA-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/AmstelvarAlpha-YTRA-max.ufo", name="AmstelvarAlpha-YTRA-max.ufo", location=dict(ytransparent=1200), styleName="YTRA-max", familyName=familyName, copyInfo=False),
]
axes = [
	dict(minimum=100, maximum=900, default=400, name="weight", tag="wght", labelNames={"en": "Weight"}, map=[]),
	dict(minimum=35, maximum=100, default=100, name="width", tag="wdth", labelNames={"en": "Width"}, map=[]),
	dict(minimum=10, maximum=72, default=14, name="opticalsize", tag="opsz", labelNames={"en": "Optical Size"}, map=[]),
	dict(minimum=5, maximum=500, default=88, name="xopaque", tag="XOPQ", labelNames={"en": "x opaque"}, map=[]),
	dict(minimum=42, maximum=402, default=402, name="xtransparent", tag="XTRA", labelNames={"en": "x transparent"}, map=[]),
	dict(minimum=4, maximum=85, default=50, name="yopaque", tag="YOPQ", labelNames={"en": "y opaque"}, map=[]),
	dict(minimum=445, maximum=600, default=500, name="lcytransparent", tag="YTLC", labelNames={"en": "lc y transparent"}, map=[]),
	dict(minimum=0, maximum=48, default=18, name="serifheight", tag="YTSE", labelNames={"en": "Serif height"}, map=[]),
	dict(minimum=88, maximum=150, default=88, name="grade", tag="GRAD", labelNames={"en": "Grade"}, map=[]),
	dict(minimum=800, maximum=1200, default=1000, name="xtransch", tag="XTCH", labelNames={"en": "x transparent Chinese"}, map=[]),
	dict(minimum=800, maximum=1200, default=1000, name="ytransch", tag="YTCH", labelNames={"en": "y transparent Chinese"}, map=[]),
	dict(minimum=650, maximum=850, default=750, name="ytransas", tag="YTAS", labelNames={"en": "y transparent ascender"}, map=[]),
	dict(minimum=150, maximum=350, default=250, name="ytransde", tag="YTDE", labelNames={"en": "y transparent descender"}, map=[]),
	dict(minimum=650, maximum=950, default=750, name="ytransuc", tag="YTUC", labelNames={"en": "y transparent uppercase"}, map=[]),
	dict(minimum=800, maximum=1200, default=1000, name="ytransparent", tag="YTRA", labelNames={"en": "y transparent"}, map=[]),
	dict(minimum=38, maximum=250, default=88, name="paraweight", tag="PWGT", labelNames={"en": "Para Weight"}, map=[]),
	dict(minimum=60, maximum=402, default=402, name="parawidth", tag="PWDT", labelNames={"en": "Para Width"}, map=[]),
]

instances = [
	#dict(location=dict(weight=38), styleName="Thin", familyName=familyName),
	#dict(location=dict(weight=60), styleName="Light", familyName=familyName),
	#dict(location=dict(weight=90), styleName="Regular", familyName=familyName),
	#dict(location=dict(weight=140), styleName="Medium", familyName=familyName),
	#dict(location=dict(weight=200), styleName="Bold", familyName=familyName),
	#dict(location=dict(weight=250), styleName="Black", familyName=familyName),
]

#for source in sources:
#	instances.append(dict(location=source["location"], styleName=source["styleName"], familyName=source["familyName"]))

### 

doc = DesignSpaceDocument()

for source in sources:
	s = SourceDescriptor()
	s.path = source["path"]
	s.name = source["name"]
	s.copyInfo = source["copyInfo"]
	s.location = source["location"]
	s.familyName = source["familyName"]
	s.styleName = source["styleName"]
	doc.addSource(s)

for instance in instances:
	i = InstanceDescriptor()
	i.location = instance["location"]
	i.familyName = instance["familyName"]
	i.styleName = instance["styleName"]
	doc.addInstance(i)

for axis in axes:
	a = AxisDescriptor()
	a.minimum = axis["minimum"]
	a.maximum = axis["maximum"]
	a.default = axis["default"]
	a.name = axis["name"]
	a.tag = axis["tag"]
	for languageCode, labelName in axis["labelNames"].items():
		a.labelNames[languageCode] = labelName
	a.map = axis["map"]
	doc.addAxis(a)

#doc.checkAxes()

#doc.checkDefault()

doc.write(designSpacePath)
