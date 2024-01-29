# Given a string, remove any characters that are unique from the string.
#
# Example:
#
# input: "abccdefee"
#
# output: "cceee"

def only_duplicates(st: str):
    set_letter = set(st)
    for i in set_letter:
        if st.count(i) < 2:
            st = st.replace(i, '')
    return st


assert only_duplicates('abccdefee') == 'cceee'
assert only_duplicates('hello') == 'll'
assert only_duplicates('colloquial') == 'ollol'
assert only_duplicates('foundersandcoders') == 'ondersndoders'
assert only_duplicates('12314256aaeff') == '1212aaff'
