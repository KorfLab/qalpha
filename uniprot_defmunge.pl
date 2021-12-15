while (<>) {
	if (/^>/) {
		my ($id, $desc) = split(/\s/, $_, 2);
		my ($tr, $i1, $i2) = split(/\|/, $id);
		print ">$i2 $i1 $desc";
	} else {
		print;
	}
}
