#!/usr/bin/python
import gnupg
from pprint import pprint
import os
import yaml
import argparse

gpg = gnupg.GPG(gnupghome='/home/vagrant/.gnupg')
#Listing keys
#public_keys = gpg.list_keys()
#private_keys = gpg.list_keys(True)
#print 'public keys:'
#pprint(public_keys)
#print 'private keys:'
#pprint(private_keys)

#Decrypt file
#f = open("foobaryaml.yml.gpg", 'r')
#enc_data = f.read()
#print('opening gpg file')
#decrypted_data = gpg.decrypt(enc_data, passphrase="ansible")
#print ('ok: ', decrypted_data.ok)
#print ('status: ', decrypted_data.status)
#print ('stderr: ', decrypted_data.stderr)
#f.close()
#print str(decrypted_data)


def OpenDictionary(SAVEFILE,PASSWORD):
 """ open the dictionary file """
 try:
     if os.path.isfile(SAVEFILE):
         f = open(SAVEFILE, 'r')
         enc_data = f.read()
         pprint('opening gpg file')
         decrypted_data = gpg.decrypt(enc_data, passphrase=PASSWORD)
         #print ('ok: ', decrypted_data.ok)
         #print ('status: ', decrypted_data.status)
         #print ('stderr: ', decrypted_data.stderr)
         f.close()
	 dict = str(decrypted_data)
	 return dict
	 #dictionary = pickle.loads(decrypted_data.data)
 except Exception as e:
     pprint('Something Snaggy happened in the call OpenDictionary(), it looks like: ', e)

parser = argparse.ArgumentParser()
parser.add_argument ('-e', '--encryptedfile', help='Used to pass the path to a GPG encrypted file')
args = parser.parse_args()
EncryptedFile = args.encryptedfile
if not EncryptedFile:
	parser.error('Needs an encrypted gpg file')

myyaml = OpenDictionary(EncryptedFile,"ansible")
try:
  yaml.load(myyaml)
  print myyaml
except:
  print str(EncryptedFile) + ' is not a valid YAML encrypted file'
