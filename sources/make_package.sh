#rm -rf michaelJEU/
#svn export .  michaelJEU/
#tar -czpf michaelJEU.tar.gz michaelJEU/
git archive master | bzip2 > MICshooter.tar.bz2
scp MICshooter.tar.bz2 michael@thenault.hd.free.fr:/var/www/dossier_upload/
#rm -rf michaelJEU/
rm MICshooter.tar.bz2
echo "http://thenault.hd.free.fr/dossier_upload/michaelJEU.tar.gz"
