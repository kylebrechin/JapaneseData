
; emergency escape
Escape::ExitApp

;ROW BELOW
F4::
Send {Alt} 
Send s
Send r
Send b

return





; ******************
; AUTO FILL
; ******************



; ONE LINE
:*:--1::
Send <sup>1</sup> `
Return

; TWO LINES
:*:--2::
Send <sup>1</sup> <br>
Send {Control down}{Enter}
Send {Control up}
Send <sup>2</sup> `
Send {Up}
Return

; THREE LINES
:*:--3::
Send <sup>1</sup> <br>
Send {Control down}{Enter}
Send {Control up}
Send <sup>2</sup> <br>
Send {Control down}{Enter}
Send {Control up}
Send <sup>3</sup> `
Send {Up 2}
Return

















; ################################################
; ################################################
; ################################################
; ################################################
; ################################################
;			NO LONGER USED FUNCTIONS
; ################################################
; ################################################
; ################################################
; ################################################














;	KanjiNumber = 1861
;	
;	
;	
;	
;	HowManyTimes(TIMES, KanjiNumber) {
	;	; move to column to fill with X's
;	Send {Left 6}
	;	; select rows
;	Send {Shift down} 
;	Send {Up %TIMES%} 
;	Send {Shift up}
	;	; fill with X's
;	Send x
;	Send {Alt down}{Enter}
;	Send {Alt up}
;	
	;	; move to KANJI row
;	Send {Left 2}
	;	; select rows
;	Send {Shift down} 
;	Send {Up %TIMES%} 
;	Send {Shift up}
	;	; fill with kanji #'s
;	Send %KanjiNumber%
;	Send {Alt down}{Enter}
;	Send {Alt up}
;	Send {Down}
;	
	;	; next KANJI
;	KanjiNumber := KanjiNumber + 1
;	Send %KanjiNumber%
;	Send {Right}
;	Send x
;	Send {Right 5}
;	
;	return KanjiNumber
;	}
;	
;	
;	F4::
;	InputBox, times, , , , , , , , , , 5
;	count := times -1
;	Sleep 200
;	KanjiNumber := HowManyTimes(count, KanjiNumber)
;	return






; #############################
;	Copy entire column over
; #############################

;	F4::
;	Loop, 300
;	{	
	;	Sleep 250
	;	Send {Alt down}{Tab}{Alt up}		; ** ALT-TAB **
	;	Sleep 250
	;	Send {F2}							; ** EDIT CELL **
	;	Sleep 250
	;	Send {Ctrl down}a{Ctrl up}			; ** SELECT ALL **
	;	Sleep 250
	;	Send {Ctrl down}c{Ctrl up}			; ** COPY **
	;	Sleep 250
	;	Send {Escape}						; ** CLOSE SELECT ALL **
	;	Sleep 250
	;	Send {Down}							; ** DOWN**
	;	Sleep 250
	;	Send {Alt down}{Tab}{Alt up}		; ** ALT-TAB **
	;	Sleep 250
	;	Send {Ctrl down}v{Ctrl up}			; ** PASTE **
	;	Sleep 250
	;	Send {Down}							; ** DOWN**
	;	Sleep 250
;	}
;	return




;			; ** ALT-TAB **
	;	Sleep 250
	;	Send {F2}							; ** EDIT CELL **
	;	Sleep 250
	;	Send {Ctrl down}a{Ctrl up}			; ** SELECT ALL **
	;	Sleep 250
	;				; ** COPY **


;	F4::
	;	; get first
;	Send {Ctrl down}x{Ctrl up}
;	Sleep 50
;	Send {Alt down}{Tab}{Alt up}
;	Sleep 50
	;	; paste first
;	Send {Ctrl down}v{Ctrl up}
;	Sleep 50
;	Send {Right 3}
	;	; get second
;	Send {Alt down}{Tab}{Alt up}
;	Sleep 50
;	Send {Ctrl down}{Right 2}
;	Sleep 50
;	Send {Shift down}{Left}
;	Sleep 50
;	Send {Shift up}x{Ctrl up}
;	Send {Alt down}{Tab}{Alt up}
;	Sleep 50
;	Send {Ctrl down}v{Ctrl up}
;	Sleep 50
;	Send {Left 3}
;	Sleep 50
;	Send {Down}
;	return
;	
;	
;	
;	
;	F5::
;	Send {Ctrl down}a{Ctrl up}			; ** SELECT ALL **
;	Send {Ctrl down}x{Ctrl up}
;	Send {Return}
;	return
;	
;	F6::
;	Send {Ctrl down}v{Ctrl up}
;	return
;	
;	F7::
;	Send {Ctrl down}{Shift down}k
;	Send {Ctrl up}{Shift up}
;	return
;	