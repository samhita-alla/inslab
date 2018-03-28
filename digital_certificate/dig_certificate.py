from OpenSSL import crypto, SSL
from time import gmtime

def create_self_signed_cert():
  
  k = crypto.PKey()
  k.generate_key(crypto.TYPE_RSA, 1024)

  # create a self-signed cert
  cert = crypto.X509()
  cert.set_serial_number(1000)
  cert.gmtime_adj_notBefore(0)
  cert.gmtime_adj_notAfter(10*365*24*60*60)
  cert.get_subject().CN = 'test certificate'
  cert.set_issuer(cert.get_subject())
  cert.set_pubkey(k)
  cert.sign(k, 'sha256')
        
  with open('test_certificate.crt','w') as certfile:
    certfile.write(crypto.dump_certificate(crypto.FILETYPE_PEM,cert))
    certfile.close()
  with open('test_private_key.key','w') as keyfile:
    keyfile.write(crypto.dump_privatekey(crypto.FILETYPE_PEM,k))
    keyfile.close()
        
create_self_signed_cert()
