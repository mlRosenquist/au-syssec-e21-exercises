#cert_0
Modulus=0x8CF9FEEF8C86FA88382B93484658C4C1EB0B389CFF74B03F91C7E899C5BB6B8317971D71D10E4B202FD478C565F60619DB785EB96715545F5E1AC186BA5268A9E6513C2C3B9E388425B17B427533957ED41898853EFDC7D95EE2476958C259524FE851B61574F85DB503E82EF9EE18FBAF0A90E6EF6814C78688562A4ED62B559B084E71F741D144DE55993A2031A41315BE6274AB6C8EEDC1F32FD2F3D4546DF90689F6234ACFDFD4A9CCE5552618F506BA175AB27DCD7A1CA519F0A6023EA67972D8FD9FED48759E75171D0D9122215F3FB47A1C617B79BB1D87C47E1A166008FAFD85F8FEE533B5B93BEDE00BE03C52C8B0FFA39F53EACCF245EB39CEB45F
Exponent=65537
Hash=0x04f21c85b9dafcc110c7885d6a879e0cf754e1ed43ae725f1520cb762b34069c
Signature=0x702df0cffa0cff7a3d3366d07f2d351ef2d5ba00d96fbab1eedc1ab66d4f05602a2c5048681b3a0dc531160a7bac229e21c4f766d5b8ffe8ff1eb072cf6b219a9d1dbae671d648a56a98dc022fe77ad9ae253eb53359277fb5bdbbbec0b41a3b358b2e30cff604d786fd7aac9efe77a7b7466166ff726e5d91ff5fa3748a87c5389196be4e7b6a24b239097c5901b5505421ff27cf4effc5e822f3643ddb268c627c0c3bfae2d77f72cd278ed326a95c202ddde815e4497d8d409b143a88084bd9283e8abab053b92e93025d4b5fc0f3ec0d61251c6e3b688f74c561615ad04e076b3105a95b0805b6d14b9672cbbd890a1d4ef374c761c2c8ed74b74259d5f0


print("Certificate 0:")
print(hex(pow(Signature, Exponent, Modulus)))
#cert_1
Modulus=0xC14BB3654770BCDD4F58DBEC9CEDC366E51F311354AD4A66461F2C0AEC6407E52EDCDCB90A20EDDFE3C4D09E9AA97A1D8288E51156DB1E9F58C251E72C340D2ED292E156CBF1795FB3BB87CA25037B9A52416610604F571349F0E8376783DFE7D34B674C2251A6DF0E9910ED57517426E27DC7CA622E131B7F238825536FC13458008B84FFF8BEA75849227B96ADA2889B15BCA07CDFE951A8D5B0ED37E236B4824B62B5499AECC767D6E33EF5E3D6125E44F1BF71427D58840380B18101FAF9CA32BBB48E278727C52B74D4A8D697DEC364F9CACE53A256BC78178E490329AEFB494FA415B9CEF25C19576D6B79A72BA2272013B5D03D40D321300793EA99F5
Exponent=65537
Hash=0x4fcc406b51cee0544e516ce74b53b5484f7371f2be5b18e463b30faa6a285971
Signature=0x77abb77a273daebbf67fe05a56c984aaca5b7117dd2247fc4e9feed0c1a404e1a3ebc549c1fdd1c9df8caf94452c462aa3633920f99e4a249441c8a9d9e29c540506cb5c1cbe001b0fa85aff19bb65c716af2156dd6105c9e98f9876df6b1bd0720c50b930297abf60591066133a2dac15116c2d230c023e053bfee5a19ce28adb87d74ae85ee74806ebab129af2af84c35b834a998183ab00a1ca0a3c4ca225892a22a7a4f3334c5b8c2e1a02970f9d8f6d2d9508fb4fdaf1913825e19c6e6118876aceb1bb00306a9bb7afdaf1c597fe8a7824aaea9380ba33657abca177e97f69140b003f7792b14d5b73870a13d09cc8f24b394f528449a64c904e1ff7b4

print("Certificate 1:")
print(hex(pow(Signature, Exponent, Modulus)))

#cert_2
Modulus=0xE23BE11172DEA8A4D3A357AA50A28F0B7790C9A2A5EE12CE965B010920CC0193A74E30B753F743C46900579DE28D22DD870640008109CECE1B83BFDFCD3B7146E2D666C705B37627168F7B9E1E957DEEB748A308DAD6AF7A0C3906657F4A5D1FBC17F8ABBEEE28D7747F7A78995985686E5C23324BBF4EC0E85A6DE370BF7710BFFC01F685D9A844105832A97518D5D1A2BE47E2276AF49A33F84908608BD45FB43A84BFA1AA4A4C7D3ECF4F5F6C765EA04B37919EDC22E66DCE141A8E6ACBFECDB3146417C75B299E32BFF2EEFAD30B42D4ABB74132DA0CD4EFF881D5BB8D583FB51BE84928A270DA3104DDF7B216F24C0A4E07A8ED4A3D5EB57FA390C3AF27
Exponent=65537
Hash=0x68538fc7818e81d2422a9060636fa5282a43f60dce1bba60c2d7f3abab660097
Signature=0xcb9c37aa4813120afadd449c4f52b0f4dfae04f5797908a32418fc4b2b84c02db9d5c7fef4c11f58cbb86d9c7a74e79829ab11b5e370a0a1cd4c8899938c9170e2ab0f1cbe93a9ff63d5e40760d3a3bf9d5b09f1d58ee353f48e63fa3fa7dbb466df6266d6d16e418df22db5ea774a9f9d58e22b59c04023ed2d2882453e7954922698e08048a837eff0d6796016deace80ecd6eac4417382f49dae1453e2ab93653cf3a5006f72ee8c457496c612118d504ad783c2c3a806ba7ebaf1514e9d889c1b9386ce2916c8aff64b977255730c01b24a3e1dce9df477cb5b424080530ec2dbd0bbf45bf50b9a9f3eb980112adc888c698345f8d0a3cc6e9d595956dde

print("Certificate 2:")
print(hex(pow(Signature, Exponent, Modulus)))