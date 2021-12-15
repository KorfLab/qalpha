qalpha
======

Quality Assessment using Alpha Fold DB

To run:

	conda install biopython
	conda activate

## Test data build ##

Starting from the build directory

	cd build

Download nematode portion of TREMBL 2021_04 from Uniprot website. Filtering based on taxonomy to nematode part of the tree.

The uniprot deflines don't work with ab-blast because they don't actually follow the ncbi spec. Therefore there is a `uniprot_defmunge.pl` script to modify them. Your command may look something like this depending on the names and locations of your files.

	gunzip -c nematodes.fasta.gz | perl ../uniprot_defmung.pl > nematodes.fasta

Make the blast database. This assumes you have installed ab-blast. It's free for personal use and better than ncbi-blast, so go get it.

	xdformat -p nematodes.fasta

Also index it so we can retrieve stuff later.

	xdformat -p -X nematodes.fasta

You should have the following files present.

	nematodes.fasta     nematodes.fasta.xpd  nematodes.fasta.xps
	nematodes.fasta.gz  nematodes.fasta.xpi  nematodes.fasta.xpt

You can get rid of the nematodes.fasta and nematodes.fasta.gz files if you want to save space.

Get a representative sequence from the fasta file.

	xdget -p nematodes.fasta A0A0K3AUW1_CAEEL > A0A0K3AUW1_CAEEL

Search it against the rest of the sequences.

	ab-blastp nematodes.fasta A0A0K3AUW1_CAEEL W=5 mformat=2 > blast.txt

Get the identifiers of some sequences that match well.

	head -25 blast.txt | cut -f 2 | sort -u > top21.txt

Build a fasta file from those sequence identifiers.

	xdget -f -p nematodes.fasta top21.txt > top21.fa

Generate a multiple alignment with whatever your favorite multiple alignment software is.

	clustalw top21.fa
	t_coffee top21.fa

Save this for later.

	mv top21.fa ../example.fa
