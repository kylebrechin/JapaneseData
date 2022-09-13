#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; --------- GUI DOCS
; https://www.autohotkey.com/docs/commands/Gui.htm

gui, font, S12
gui, Add, Checkbox, checked 1 vahk, test.com
gui, Show, W500 H500
return




; emergency exit
^Escape::ExitApp
