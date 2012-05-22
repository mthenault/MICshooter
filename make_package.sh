rm -rf michaelJEU/
svn export .  michaelJEU/
tar -czpf michaelJEU.tar.gz michaelJEU/
scp michaelJEU.tar.gz michael@thenault.hd.free.fr:/var/www/dossier_upload/
rm -rf michaelJEU/
rm michaelJEU.tar.gz
echo "http://thenault.hd.free.fr/dossier_upload/michaelJEU.tar.gz"
