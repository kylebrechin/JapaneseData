; default shit
#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

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
	inputbox text
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
return

^NumpadSub::
	InputBox, Zeroes, Rows, How many rows to add:, , 300, 100
	Loop, %Zeroes% {
		RunMain(0)
	}
	EndSound()
	
return



NumpadAdd::
	GetRowCount()
	EndSound()
return

NumpadDot::
	ScrollScreenRowsDown()
return

NumpadDiv::
	SwitchApplication()
return
