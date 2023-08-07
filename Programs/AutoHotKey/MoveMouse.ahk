
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Escape::ExitApp

#m::
Loop {
	MouseMove, 10, 0, 80
	Sleep 30000
	MouseMove, -10, 0, 80
	Sleep 30000
}
return