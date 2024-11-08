def main():
	userinput = input("Enter the ascii codes\n")


def parse_response(ascii_codes):
	splitted_codes = ascii_codes.split(',')
	if splitted_codes < 97 or splitted_codes > 122:
		return "Not valid"
	string = ""
	match splitted_codes:
		case 97:
			string += 'a'
		case 98:
			string += 'b'
		case 99:
			string += 'c'
		case 100:
			string += 'd'
		case 101:
			string += 'e'
		case 102:
			string += 'f'
		case 103:
			string += 'g'
		case 104:
			string += 'h'
		case 105:
			string += 'i'
		case 106:
			string += 'j'
		case 107:
			string += 'j'
		case 108:
			string += 'k'
		case 109:
			string += 'l'
		case 110:
			string += 'm'
		case 111:
			string += 'n'
		case 112:
			string += 'o'
		case 113:
			string += 'p'
		case 114:
			string += 'q'
		case 115:
			string += 'r'
		case 116:
			string += 's'
		case 117:
			string += 't'
		case 118:
			string += 'u'
		case 119:
			string += 'v'
		case 120:
			string += 'w'
		case 121:
			string += 'x'
		case 122:
			string += 'y'
		