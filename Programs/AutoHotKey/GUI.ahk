#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


; --------- GUI DOCS
; https://www.autohotkey.com/docs/commands/Gui.htm

gui, font, S12
; Wn Hn Xn Yn 
gui, Add, Button, w80, Click
gui, Show, W200 H200
return











; =============== DOCUMENTATION
; Gui, Add, Button, w200 h50 gTest1 , Run Test1.AHK Script
; Gui, Add, Button, w200 h50 gTest2 , Run Test2.AHK Script
; Gui, Show,, Print Options
; Return
; 
; Test1:
; Run test_script1.ahk
; Return
; 
; Test2:
; Run test_script2.ahk
; Return
; 
; GuiClose:
; ExitApp