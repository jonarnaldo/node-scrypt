{
    'targets' : [
        {
            'target_name': 'scrypt',
            'defines': [
                'HAVE_CONFIG_H'                
            ],
            'include_dirs' : [
                'scrypt-1.1.6',
                'scrypt-1.1.6/lib/util',
                'scrypt-1.1.6/lib/crypto',
                'scrypt-1.1.6/lib/scryptenc'
            ],
            'sources': [
                'scrypt_crypto.cc',
                'scrypt-1.1.6/lib/scryptenc/scryptenc.c',
                'scrypt-1.1.6/lib/util/memlimit.c',
                'scrypt-1.1.6/lib/scryptenc/scryptenc_cpuperf.c',
                'scrypt-1.1.6/lib/crypto/sha256.c',
                'scrypt-1.1.6/lib/crypto/crypto_aesctr.c',
                'scrypt-1.1.6/lib/crypto/crypto_scrypt-ref.c'
            ],
            'conditions': [
                ['OS == "linux"', {
                    'link_settings': {
                        'libraries': [
                            '-lcrypto', #The openssl library (libcrypto)
                            '-lrt' #RealTime library
                        ],
                    },
                }]
            ],
        },
    ],
}
