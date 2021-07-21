#! /usr/bin/fish

# fish prompt
function fish_prompt
	set -l LastStatus $status
	set -l dir (pwd)

	# err color handle
	if not test $LastStatus -eq 0
		set -g ErrColor "$red!"
	else
		set -g ErrColor "$green"
	end


	# string replacing for simpler dir names
		set -l dir (string replace '/home/owsei' '~' $dir)
		set -l dir (string replace '~/Documents' 'docs' $dir)
		set -l dir (string replace '~/Desktop' 'desk' $dir)
		set -l dir (string replace '~/Pictures' 'pics' $dir)
		set -l dir (string replace '~/Videos' 'vids' $dir)
		set -l dir (string replace '~/BDP' 'BDP' $dir)
		set -l dir (string replace 'docs/py' 'PyD' $dir)
		set -l dir (string replace 'docs/js' 'JsD' $dir)
		set -l dir (string replace 'docs/c#' 'CsD' $dir)
      	set -l dir (string replace '~/.config' 'configs' $dir)	
		set -l dir (string replace 'configs/fish' '><>' $dir)
		set -l dir (string replace 'PyD/FCP' 'FakeCursesPython' $dir)


	#end
	# [λ, >>>, ➢, ⟹, ●, ┍ ┫ ┣ ┕, ]
	# show err color [err num] and "$pointer"
	set -l pointer '┕'
	printf "$BrCyan┍┫$red$USER$nc $BrCyan$dir$nc $ErrColor""[$LastStatus]$nc\n$BrCyan$pointer$nc"
end
