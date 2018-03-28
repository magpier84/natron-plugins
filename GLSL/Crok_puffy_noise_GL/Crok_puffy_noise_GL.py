# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_puffy_noise_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_puffy_noise_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_puffy_noise_GL"

def getLabel():
    return "Crok_puffy_noise_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Crok_puffy_noise_GL.png"

def getGrouping():
    return "Community/GLSL/Source"

def getPluginDescription():
    return "Simulates puffy noise.\n( https://vimeo.com/82495451 )"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.6235, 0.3451, 0.7647)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat0", "Rotation : ")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1000, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("rotation")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat2", "Speed : ")
    param.setMinimum(-10000, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(-5000, 0)
    param.setDisplayMaximum(5000, 0)
    param.setDefaultValue(5, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("speed\n")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool1", "Vignette : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("vignette")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool1 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_puffy_noise_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4320)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3992)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueBool1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("#ifdef GL_ES\nprecision mediump float;\n#endif\n\n\nuniform float Rotation = 0.0; // Rotation : , min=0.0, max=10000\nuniform float pLeft;\nuniform bool vignette = false; // Vignette : \n\nvec2 resolution = vec2(iResolution.x, iResolution.y);\nvec2 mouse = vec2(Rotation, pLeft);\nfloat globalltime = iTime*.05;\n\nuniform float time = 5.0; // Speed : ,min=-10000, max=10000\n\n// Created by inigo quilez - iq/2013\n// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.\n// original here: https://www.shadertoy.com/view/MsXGRf - please preserve credits in downstream experiments.\n\n\n// hash based 3d value noise\nfloat hash( float n )\n{\n    return fract(sin(n)*43758.5453);\n}\nfloat noise( in vec3 x )\n{\n    vec3 p = floor(x);\n    vec3 f = fract(x);\n\n    f = f*f*(3.0-2.0*f);\n    float n = p.x + p.y*57.0 + 113.0*p.z;\n    return mix(mix(mix( hash(n+  0.0), hash(n+  1.0),f.x),\n                   mix( hash(n+ 57.0), hash(n+ 58.0),f.x),f.y),\n               mix(mix( hash(n+113.0), hash(n+114.0),f.x),\n                   mix( hash(n+170.0), hash(n+171.0),f.x),f.y),f.z);\n}\n\n\nvec4 map( vec3 p )\n{\n\tvec3 r = p;\n\t\n\tfloat den = -0.6 - p.y;\n    // invert space\t\n   // p.y += 0.6;\n\tp = -2.0*p/dot(p,p);\n\n\n    // twist space\t\n\tfloat an = -1.0*sin(0.1*time*globalltime + 1.0*length(p.xz)  + 1.0*p.y);\n\tfloat co = cos(an);\n\tfloat si = sin(an);\n\tp.xz = mat2(co,-si,si,co)*p.xz;\n\n     // distort\t\n\tp.xz += 1.0*(-1.0+2.0*noise( p*1.1 ));\n\n    // pattern\n\tfloat f;\n\tvec3 q = p*0.85                     - vec3(0.0,1.0,0.0)*time*globalltime*0.12;\n    f  = 0.50000*noise( q ); q = q*2.02 - vec3(0.0,1.0,0.0)*time*globalltime*0.12;\n    f += 0.25000*noise( q ); q = q*2.03 - vec3(0.0,1.0,0.0)*time*globalltime*0.12;\n    f += 0.12500*noise( q ); q = q*2.01 - vec3(0.0,1.0,0.0)*time*globalltime*0.12;\n    f += 0.06250*noise( q ); q = q*2.02 - vec3(0.0,1.0,0.0)*time*globalltime*0.12;\n    f += 0.04000*noise( q ); q = q*2.00 - vec3(0.0,1.0,0.0)*time*globalltime*0.12;\n\n\tden = clamp( (den + 4.0*f)*1.2, 0.0, 1.0 );\n\t\n\tvec3 col = 1.2*mix( vec3(1.0,0.8,0.6), 0.9*vec3(0.3,0.2,0.35), den ) ;\n\tcol += 0.05*sin(0.05*q);\n\t//col *= 1.0 - 0.8*smoothstep(0.6,1.0,sin(0.7*q.x)*sin(0.7*q.y)*sin(0.7*q.z))*vec3(0.6,1.0,0.8);\n\t//col *= 1.0 + 1.0*smoothstep(0.5,1.0,1.0-length( (fract(q.xz*0.12)-0.5)/0.5 ))*vec3(1.0,0.9,0.8) ;\n\tcol = mix( vec3(0.8,0.3,0.2), col, clamp( (r.y+0.1)/1.5, 0.0, 1.0 ) );\n\n\treturn vec4( col, den );\n}\n\n\nvec3 raymarch( in vec3 ro, in vec3 rd )\n{\n\tvec4 sum = vec4( 0.0 );\n\tvec3 bg = vec3(0.4,0.5,0.5)*1.3;\n\n\tfloat t = 0.0;\n\t\n\t// dithering\n\t// t += 0.05*texture2D( iChannel0, fragCoord.xy/iChannelResolution[0].x ).x;\n\n\t\n\tfor( int i=0; i<128; i++ )\n\t{\n\t\tif( sum.a > 0.99 ) continue;\n\t\tvec3 pos = ro + t*rd;\n\t\tvec4 col = map( pos );\n\t\t\n\t\tcol.xyz = mix( bg, col.xyz, exp(-0.002*t*t*t) );\n\t\t\n\t\tcol.a *= 0.5;\n\t\tcol.rgb *= col.a;\n\n\t\tsum = sum + col*(1.0 - sum.a);\t\n\t\t\n\t\tt += 0.05;\n\t\t\n\t}\n\n\tsum.xyz = mix( bg, sum.xyz/(0.001+sum.w), sum.w );\n\treturn clamp( sum.xyz, 0.0, 1.0 );\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n    // inputs\t\n    vec2 q = fragCoord.xy / resolution.xy;\n    vec2 p = -1.0 + 2.0*q;\n    p.x *= resolution.x/ resolution.y;\n\t\n    vec2 mo = mouse.xy / resolution.xy;\n    if( mouse.x<=0.00001 ) mo=vec2(0.0);\n\t\n    // camera\n\tfloat an = -0.07*time*globalltime + 3.0*mo.x;\n    vec3 ro = 4.5*normalize(vec3(cos(an), 0.5, sin(an)));\n\tro.y += 1.0;\n\tvec3 ta = vec3(0.0, 0.5, 0.0);\n\tfloat cr = -0.4*cos(0.02*time*globalltime);\n\t\n\t// build ray\n    vec3 ww = normalize( ta - ro);\n    vec3 uu = normalize(cross( vec3(sin(cr),cos(cr),0.0), ww ));\n    vec3 vv = normalize(cross(ww,uu));\n    vec3 rd = normalize( p.x*uu + p.y*vv + 2.5*ww );\n\t\t\n    // raymarch\t\n\tvec3 col = raymarch( ro, rd );\n\t\n\t// contrast\n\tcol = col*col*(3.0-2.0*col)*1.4 - 0.4;\n\t\n    col.y *= 1.05;\t\n    \n    // vignetting\t\t\n\tif (vignette)\n\t{\n\t\tcol *= 0.25 + 0.75*pow( 16.0*q.x*q.y*(1.0-q.x)*(1.0-q.y), 0.1 );\n\t\tfragColor = vec4( col, 1.0 );\n\t}\n    \n    fragColor = vec4( col, 1.0 );\n}\n\n\n\n")
        del param

    param = lastNode.getParam("inputEnable0")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("Rotation")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Rotation :")
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(10000, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("vignette")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Vignette :")
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("time")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Speed :")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(-10000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(10000, 0)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)

    param = groupShadertoy1_2.getParam("paramValueFloat0")
    group.getParam("Shadertoy1_2paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool1")
    group.getParam("Shadertoy1_2paramValueBool1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat2")
    group.getParam("Shadertoy1_2paramValueFloat2").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Crok_puffy_noise_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
