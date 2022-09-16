; default shit

;#NoEnv
;SendMode Input
;SetWorkingDir %A_ScriptDir%

#Include functions.ahk

KKLC_line_num := ""
KKLC_kanji := ""
KKLC_kana := ""
KKLC_meaning := ""
KKLC_notes := ""
lines := 0


; MAY BE USEFUL LATER
; prompt # items
; prompt: enter "notes" count ie [0, 0, 1, 0, 1, 1]
; have the program autocomplete :D

; inputbox text
; array := strsplit(text, `,)
; random n, 1, array.length()
; send % array[n]

NumpadSub::
	if WinActive("ahk_exe sublime_text.exe") {
		inputbox text
		if(ErrorLevel = 0) {
			notes_array := strsplit(text, A_Space)
			for useless, number in notes_array
			{
				switch, number
				{
					case 0:
						RunMain(0)
					case 1:
						RunMain(1)
					case 2:
						RunMain(2)
					case 3:
						RunMain(3)
					case 4:
						RunMain(4)
					case 5:
						RunMain(5)
					case 6:
						RunMain(6)
					case 7:
						RunMain(7)
					case 8:
						RunMain(8)
					case 9:
						RunMain(9)
				}
				CompleteSound()
			}
			EndSound()
		}
		else {
			ErrorSound()
		}

	}
	else {
		ErrorSound()
	}

return

^NumpadSub::
	if WinActive("ahk_exe sublime_text.exe") {
		InputBox, Zeroes, Rows, How many rows to add:, , 300, 100
		if(ErrorLevel = 0) {
			Loop, %Zeroes% {
				RunMain(0)
			}
			EndSound()
		}
		else {
			ErrorSound() 
		}
	}
	else {
		ErrorSound()
	}

return

^NumpadAdd::
	if WinActive("ahk_exe soffice.bin") {
		InputBox, Naturals, Rows, How many rows and naturals:, , 300, 100
		if(ErrorLevel = 0) {
			Sleep, 100
			RowCount(Naturals)
			Sleep, 100
			; Set Item Number here

			Loop, %Naturals% {
				RunMain(0)
			}
			EndSound()
		}
		else {
			ErrorSound()
		}
	} 
	else {
		ErrorSound()
	}
return


NumpadMult::
	WinActivate, KKLC_study_complete.ods - LibreOffice Calc
	Sleep, 100
	WinActivate, I:\Amazon Drive BACKUP\Languages\Japanese\JapaneseData\Data\KKLC\Readers\Book_05.txt - Sublime Text (UNREGISTERED)
return









NumpadAdd::
	if WinActive("ahk_exe soffice.bin") {
		GetRowCount()
		EndSound()
	} 
	else {
		ErrorSound()
	}
return



NumpadDot::
	if WinActive("ahk_exe soffice.bin") {
		ScrollScreenRowsDown()
	} 
	else {
		ErrorSound()
	}
return

NumpadDiv::
	SwitchApplication()
return

F4::
	if WinActive("ahk_exe soffice.bin") {
	Click, 2
	Send {Shift down}
	Send {End}
	Send {Shift up}
	Send {Backspace}
	Send {Enter}
	} 
	else {
		ErrorSound()
	}

return