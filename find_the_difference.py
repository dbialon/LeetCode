# https://leetcode.com/problems/find-the-difference/
# given two strings s and t which consist of only lowercase letters.
# string t is generated by random shuffling string s
# and then add one more letter at a random position.
# find the letter that was added in t

def findTheDifference(s: str, t: str):
	result = 0
	for char in t:
		result ^= ord(char)
		
	for char in s:
		result ^= ord(char)
		
	return chr(result)


a = "xpmssbwloowxibtwvhabflaoqgoyswznxepaoevvqohhamkucbcfsonazfnmcoqechnyigsbuvzrligprykurwahetwjmdknmearurflryhligaptsdqrlgapoyzocwwnavcsdiuqpbzmedzsvifcqzjjqqjshqmxczobymhwwiojfcvfjvaygupgacyvhnckmdasgspxoijltxebfspwlpjbzpoonalwujttowlsiagmcgfqwxoznuehztvuvpgzrvrjnybfcolufwgwsgmuxdqfgcisxgeibinqxacrtwznwvmxximhhhdehxrftpcczubiabgkbscrundidaqzcbmzpiqecfruiffzuajxjnnwipeivtswffizywisuvhkkcjwgxazntusebfbaawflsazleudgmhyzgfspyqmqanozvksrougiypcmiokgdhmkwyngmrynkekfjogjpgannxdtczvgxmatirlfcsphzouosyknxigetrpzudjaxcepvdfmqfyjpvxifntszpbzfkrlxgodjecpvtljolottyhaonpvatwhynicfusbrcnfhkpglaouhmljaavvguoiyiynpqykhaqsbbdroszpawpzgjtnzmqeiuvbwhyphrhqzbaqnnusbiopkzbsovqtykfioyurtqqnspkhnllmsvkgewpslshrambdokxhrelsehvvgitcwyrhivarxjagtsgfnhudizcbmvncgjfa"
b = "wsxqlutrifhyejgmohyvlkjobelupizpgbgavnltzspgvmthdhioonnilqshpsvyejddnitnxrpmdvkudqhoajzupcxrwghhyhudsqrszojzwpcbontwdbfbqncysqzgoayjxbqkieamizzsoaqksqwjmjawwmkltcfzffruhaarhcexhenrgizwvnqfkrfhthbovxuynxoltrtagsceiiphsombaqcztfookpepwymnsxtlspgbdkmyezlzdvinemwibvsggnyfoabsfqxtgzecfiwpyqzsiilnrmugnbczsouczgfmkhunqfhpzqgyurrzpqccmvfjnbwgwrlclnvvsgbhkdfipnsinmasvryegdzuiazoisrcbgpyohvhvpujjxxtoruxpomxmjwuockcwjgpnhlfojvapaxnablqhujdtsofuiapfcjcdvxsavkavmrptqptpnxaasazuolwcltbysmezytwvmzislbasghogaqhhjqryzmbubsewcyustwguyiyvgswcefbpgrzjgvwezzmzfatatksonevbcupwtoxcjxaivqxciuklycbacoonuvvmuaazmrgguiuzyrhjbipwjpurofecklonpldgofikgijfiknaqisrmxfnvlqbwwifykjogtdqocdpffetagavwrchfiskwwecmrhhnpvlifaxkhbdapyafighonnxeamgpqnazvsnkbzrdcwyfyssseagfhlixn"
# correct output: "s"

print(findTheDifference(a, b))

x = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
y = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"
# correct output: "t"

print(findTheDifference(x, y))