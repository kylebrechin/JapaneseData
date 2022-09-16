; Sublime RegEx
; \s\s\n$
; " \n" <-- blank space, remove ""















GUITest() {
	MsgBox, "Hello there"
}











; ****************
; ********************
; *************************
; *****************************
; ================================
; 		COMPLETE FUNCTIONS
; ================================
; *****************************
; *************************
; ********************
; ****************


RunMain(lines) {
	EmptyVariables( KKLC_line_num, KKLC_kanji, KKLC_kana, KKLC_meaning, KKLC_notes)
	GetAll(KKLC_line_num, KKLC_kanji, KKLC_kana, KKLC_meaning, KKLC_notes, lines)
	SwitchApplication()
	SetAll( KKLC_line_num, KKLC_kanji, KKLC_kana, KKLC_meaning, KKLC_notes)
	SwitchApplication()
}





; ======================
;	SETTER FUNCTIONS
; ======================

SetAll( ByRef KKLC_line_num, ByRef KKLC_kanji, ByRef KKLC_kana, ByRef  KKLC_meaning, ByRef KKLC_notes) {
	SetItemNumber()
	ExampleMarker()
	SetLineNumber(KKLC_line_num)
	SetKanji(KKLC_kanji) 
	SetKana(KKLC_kana)
	SetMeaning(KKLC_meaning) 
	SetNotes(KKLC_notes) 
	ResetLinePosition()
	Sleep, 200
}

ExampleMarker() {
	Send x
	MoveRight(5)
}

SetItemNumber() {
	MoveUp()
	Sleep, 50
	CopyOne()
	Sleep, 50
	MoveDown()
	Sleep, 50
	Paste()
	Sleep, 50
	MoveRight(3)
}

SetLineNumber(KKLC_line_num) {
	clipboard := KKLC_line_num
	Sleep, 200
	Paste()
	MoveRight()
}
SetKanji(KKLC_kanji) {
	clipboard := KKLC_kanji
	Sleep, 200
	Paste()
	MoveRight(3)
}
SetKana(KKLC_kana){
	clipboard := KKLC_kana
	Sleep, 200
	Paste()
	MoveRight()
}
SetMeaning(KKLC_meaning) {
	clipboard := KKLC_meaning
	Sleep, 200
	Paste()
	MoveRight()
}
SetNotes(KKLC_notes) {
	clipboard := KKLC_notes
	Sleep, 200
	Send {F2}
	Paste()
	Sleep, 200
	Send {Return}
}


; ======================
;	GETTER FUNCTIONS
; ======================

GetAll(ByRef KKLC_line_num, ByRef KKLC_kanji, ByRef KKLC_kana, ByRef  KKLC_meaning, ByRef KKLC_notes, lines) {
	GetLineNumber(KKLC_line_num)
	GetKanji(KKLC_kanji)
	GetKana(KKLC_kana)
	GetMeaning(KKLC_meaning)
	if( lines > 0) {
		GetNotes(KKLC_Notes, lines)
		GoToNextLine()
	}
	Sleep, 200
}

GetLineNumber(ByRef KKLC_line_num) {
	SelectLineNumber()
	KKLC_line_num := Copy()
	ScrollDown()
	GoToNextLine()
}

GetKanji(ByRef KKLC_kanji) {
	SelectLine()
	KKLC_kanji := Copy()
	ScrollDown()
	GoToNextLine()
}

GetKana(ByRef KKLC_kana) {
	SelectLine()
	KKLC_kana := Copy()
	ScrollDown()
	GoToNextLine()
}

GetMeaning(ByRef KKLC_meaning) {
	SelectLine()
	KKLC_meaning := Copy()
	ScrollDown()
	GoToNextLine()
}

GetNotes(ByRef KKLC_notes, lines:=0) {
	SelectNotes(lines)
	KKLC_notes := Copy()
	ScrollDown(lines)
}


; ======================
;	UTILITY FUNCTIONS
; ======================

ResetLinePosition() {
	MoveLeft(14)
}

MoveUp() {
	Send {Up}
	Sleep, 20
}

MoveDown() {
	Send {Down}
	Sleep, 20
}

MoveLeft(moveCount:=1) {
	Loop, %moveCount% {
		Send {Left}
		Sleep, 20
	}
}

MoveRight(moveCount:=1) {
	Loop, %moveCount% {
		Send {Right}
		Sleep, 20
	}
}

GoToNextLine() {
	Send {Home}
	Sleep, 20
	Send {Down}
}

ScrollDown(times:=1) {
	Loop, %times% {
		Send ^{Down}
	}
}

ScrollScreenRowsDown() {
	SetScrollLockState, On
	Sleep, 100
	Send {Down 50}
	Sleep, 100
	SetScrollLockState, Off
	Sleep, 100
	Send {Up}
}

GetRowCount() {
	InputBox, AddRows, Rows, How many rows to add:, , 300, 100
	if(ErrorLevel = 0) {
		Sleep, 100
		Loop, %AddRows% {
			Sleep, 75
			Send {Alt} 
			Sleep, 75
			Send s
			Sleep, 75
			Send r
			Sleep, 75
			Send b
			Sleep, 100
		}
		Send {Down}
		Sleep, 100
		SwitchApplication()
	}
	else {
		ErrorSound()
	}
}

RowCount(AddRows:=1) {
	Loop, %AddRows% {
		Sleep, 75
		Send {Alt} 
		Sleep, 75
		Send s
		Sleep, 75
		Send r
		Sleep, 75
		Send b
		Sleep, 100
	}
	Send {Down}
	Sleep, 200
	SwitchApplication()
}

; ======================
;	CONTROL FUNCTIONS
; ======================

Paste() {
	Send ^v
	Sleep, 200
}

Cut() {
	Send ^x
	Sleep, 500
	return clipboard
}


CopyOne() {
	Send ^c
	Sleep, 200	
}

Copy() {
	Send ^c
	Sleep, 200
	return clipboard
}


; ======================
;	SELECTION FUNCTIONS
; ======================

SelectLineNumber() {
	Send {Ctrl down}{Shift down}
	Sleep, 50
	Send {Right}{Right}
	Sleep, 50
	Send {Shift up}{Ctrl up}
	Sleep, 50
}

SelectLine() {

	Send {Shift down}{End}{Shift up}
	Sleep, 100
}

SelectNotes(rows:=0) {
	
	switch rows {
	;case 0: 
		;Send {Shift up}
		;Sleep, 50
		;return
	case 1: 
		Sleep, 50
		SelectLine()
		return
	case 2: 
		Send {Shift down}
		Send {Down 1}
	case 3: 
		Send {Shift down}
		Send {Down 2}
	case 4: 
		Send {Shift down}
		Send {Down 3}
	case 5: 
		Send {Shift down}
		Send {Down 4}
	case 6: 
		Send {Shift down}
		Send {Down 5}
	case 7: 
		Send {Shift down}
		Send {Down 6}
	case 8: 
		Send {Shift down}
		Send {Down 7}
	case 9: 
		Send {Shift down}
		Send {Down 8}
	case 10: 
		Send {Shift down}
		Send {Down 9}
	}
	Send {End}{Shift up}
}

SwitchApplication() 
{ 
	Send {Alt down}{Tab}{Alt up} 
	Sleep, 300
}


; COPY AND PASTE TO EMPTY VARIABLES
;EmptyVariables(KKLC_line_num, KKLC_kanji, KKLC_kana, KKLC_meaning, KKLC_notes)

EmptyVariables( ByRef KKLC_line_num, ByRef KKLC_kanji, ByRef KKLC_kana, ByRef  KKLC_meaning, ByRef KKLC_notes) {
	KKLC_line_num := ""
	KKLC_kanji := ""
	KKLC_kana := ""
	KKLC_meaning := ""
	KKLC_notes := ""
	Sleep, 500
}

; emergency escape
^Escape::ExitApp


CompleteSound() {
	SoundPlay, C:\Windows\media\Windows Startup.wav
}

EndSound() {
	SoundPlay, C:\Windows\media\Windows Shutdown.wav
}

ErrorSound() {
	SoundPlay, C:\Windows\media\Windows Exclamation.wav	
}

; Useful to double click and delete last stuff in a line
; F4::
	; Click, 2
	; Send {Shift down}
	; Send {End}
	; Send {Shift up}
	; Send {Backspace}
	; Send {Enter}
; return


; F5::
	; clipboard := KKLC_line_num
	; Paste()
	; Send {Enter}
	; Sleep, 200
	; clipboard := KKLC_kanji
	; Paste()
	; Send {Enter}
	; Sleep, 200
	; clipboard := KKLC_kana
	; Paste()
	; Send {Enter}
	; Sleep, 200
	; clipboard := KKLC_meaning
	; Paste()
	; Send {Enter}
	; Sleep, 200
	; clipboard := KKLC_notes
	; Paste()
	; Send {Enter}
	; Sleep, 200
; return




;Numpad0::
	;RunMain(0)
;return
;
;Numpad1::
	;RunMain(1)
;return
;
;Numpad2::
	;RunMain(2)
;return
;
;Numpad3::
	;RunMain(3)
;return
;
;Numpad4::
	;RunMain(4)
;return
;
;Numpad5::
	;RunMain(5)
;return
;
;Numpad6::
	;RunMain(6)
;return
;
;Numpad7::
	;RunMain(7)
;return
;
;Numpad8::
	;RunMain(8)
;return
;
;Numpad9::
	;RunMain(9)
;return