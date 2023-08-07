#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; # win
; ^ ctrl
; ! alt
; 

; Win + D = open Downloads
#d::
	Run, "C:\Users\HELLHEIM\Downloads"
return

#r::
	Run, %A_MyDocuments%\ROAR documents
return
