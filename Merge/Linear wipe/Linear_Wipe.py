# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Linear_WipeExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Linear_WipeExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.LinearWipe"

def getLabel():
    return "Linear_Wipe"

def getVersion():
    return 1

def getIconPath():
    return "linearWipe_icon.png"

def getGrouping():
    return "Community/Merge"

def getPluginDescription():
    return "A Linear Wipe for Transition"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)

    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "control")
    param = lastNode.createBooleanParam("flip", "flip")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.flip = param
    del param

    param = lastNode.createDoubleParam("Linear_Wipe_StoyparamValueFloat1", "Transition")
    param.setMinimum(0, 0)
    param.setMaximum(300, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(300, 0)
    param.setDefaultValue(150, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Mid Value 150")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Linear_Wipe_StoyparamValueFloat1 = param
    del param

    param = lastNode.createDoubleParam("Linear_Wipe_StoyparamValueFloat2", "Feather")
    param.setMinimum(0.001, 0)
    param.setMaximum(2, 0)
    param.setDisplayMinimum(0.001, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(0.001, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Linear_Wipe_StoyparamValueFloat2 = param
    del param

    param = lastNode.createDoubleParam("Linear_Wipe_StoyparamValueFloat3", "Rotation")
    param.setMinimum(0, 0)
    param.setMaximum(359.9999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(359.9999999999999, 0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Linear_Wipe_StoyparamValueFloat3 = param
    del param

    param = lastNode.createDoubleParam("Linear_Wipe_StoyparamValueFloat4", "Evolution")
    param.setMinimum(1, 0)
    param.setMaximum(20, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Linear_Wipe_StoyparamValueFloat4 = param
    del param

    lastNode.credit = lastNode.createPageParam("credit", "credit")
    param = lastNode.createStringParam("Dev", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("Developed BY")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.Dev = param
    del param

    param = lastNode.createStringParam("name", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("Fahad Hasan Pathik (CGVIRUS)")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.name = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'credit', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Linear_Wipe_Stoy"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Linear_Wipe_Stoy")
    lastNode.setLabel("Linear Wipe Stoy")
    lastNode.setPosition(788, 260)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupLinear_Wipe_Stoy = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(150, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(0.001, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//Development by CGVIRUS under GNU GPL Version 3 Licence.\n\n// iChannel0: Source, filter=linear, wrap=clamp\n// BBox: iChannel0\n\n//parametres\nuniform int flip = 0; // flip, min=0, max=1\nuniform float Transition = 0.0; // Transition, min=0.0, max=300\nuniform float Feather = 0.001; // Feather, min=0.001, max=2\nuniform float rotation = .0; // Rotation , min=0.,max=360.\nuniform float Evolution = 1.0; // Evolution, min=1.0, max=20.\n\nconst float PI = 3.14159265358979323846264;\nconst float TWOPI = 6.283185307179586476925286766559;\n\nfloat makewipe(vec2 uv, vec2 pos, float Transition)\n{\n    float rot = radians(rotation+45.0)*Evolution;\n\tmat2 m = mat2(cos(rot), -sin(rot), sin(rot), cos(rot));\n   \tuv  = m*uv;\n    // pos = m*pos;\n    \n  float main = uv.x+uv.y;\n  // float ang = atan(main.y, main.x);\n  float wipe = radians(Transition*TWOPI/9.5-100.0);\n  float f0 = 0.0;\n  if (flip == 0){\n  f0 = (main+wipe)/(PI*Transition*.01*(-Feather*PI));\n  }\n  else {\n  f0 = (-main+wipe)/(PI*Transition*.01*(-Feather*PI));\n  }\n  return clamp(f0,0.0,1.0);\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 uv = fragCoord.xy / iResolution.xy;\n\tuv -= 0.5;\n\tuv.x *= iResolution.x / iResolution.y;\n\t\n\tvec2 mouse = iMouse.xy/iResolution.xy;\n\tmouse -= 0.5;\n\tmouse.x *= iResolution.x / iResolution.y;\n\t\n    vec2 xy = fragCoord.xy / iResolution.xy;\n    vec4 linker = texture(iChannel0,xy);\n\t\n\tfloat c = makewipe(uv, mouse, Transition);\n\t\n\tfragColor = vec4(vec3(c), c)*linker;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
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

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
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
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("flip")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("flip")
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("Transition")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Transition")
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(300, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("Feather")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Feather")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(0.001, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(0.001, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("rotation")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Rotation")
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(359.9999999999999, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("Evolution")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Evolution")
        del param

    param = lastNode.getParam("paramDefaultFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxFloat4")
    if param is not None:
        param.setValue(20, 0)
        del param

    del lastNode
    # End of node "Linear_Wipe_Stoy"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(788, 144)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(788, 370)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupLinear_Wipe_Stoy.connectInput(0, groupSource)
    groupOutput1.connectInput(0, groupLinear_Wipe_Stoy)

    param = groupLinear_Wipe_Stoy.getParam("paramValueInt0")
    param.setExpression("thisGroup.flip.get()", False, 0)
    del param
    param = groupLinear_Wipe_Stoy.getParam("paramValueFloat1")
    group.getParam("Linear_Wipe_StoyparamValueFloat1").setAsAlias(param)
    del param
    param = groupLinear_Wipe_Stoy.getParam("paramValueFloat2")
    group.getParam("Linear_Wipe_StoyparamValueFloat2").setAsAlias(param)
    del param
    param = groupLinear_Wipe_Stoy.getParam("paramValueFloat3")
    group.getParam("Linear_Wipe_StoyparamValueFloat3").setAsAlias(param)
    del param
    param = groupLinear_Wipe_Stoy.getParam("paramValueFloat4")
    group.getParam("Linear_Wipe_StoyparamValueFloat4").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Linear_WipeExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)