'''
Substituting Strings with the sub() method

Regular expressions can not only find text patterns but can also substitute
new text in place of those patterns. The sub() method for Regex objects is
passed two arguments. The first argument is a string to replace any matches.
The second is the string for the regular expression. The sub() method returns
a string with the substitutions applied.
'''
import re

namesRegex = re.compile(r'Agent \w+')
m = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(m) # REDACTED gave the secret documents to REDACTED.

'''
Sometimes you may need to use the matched text itself as part of the
substitution. 
In the first argument to sub(), you can type \1, \2, \3, and so
on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”

For example, say you want to censor the names of the secret agents by
showing just the first letters of their names. 
To do this, you could use the
regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1
in that string will be replaced by whatever text was matched by group 1—
that is, the (\w) group of the regular expression.
'''
agentNamesRegex = re.compile(r'Agent (\w)\w*')
m =agentNamesRegex.sub(r'Agent \1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(m) # Agent A**** told Agent C**** that Agent E**** knew Agent B**** was a double agent.


################ verbose mode
'''
Managing complex regex with Verbose mode

Regular expressions are fine if the text pattern you need to match is simple.
But matching complicated text patterns might require long, convoluted regular expressions.
You can mitigate this by telling the re.compile() function
to ignore whitespace and comments inside the regular expression string.

This “verbose mode” can be enabled by passing the variable re.VERBOSE as
the second argument to re.compile().

Now instead of a hard-to-read regular expression like this:
'''
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
'''
you can spread the regular expression over multiple lines with comments
like this:
'''
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?           # area code
(\s|-|\.)?                   # separator
\d{3}                        # first 3 digits
(\s|-|\.)                    # separator
\d{4}                        # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

############# combining the second argument in the compile method
'''
Combining re.IGNORECASE, re.DOTAll, and re.VERBOSE

What if you want to use re.VERBOSE to write comments
in your regular expression but also want to use re.IGNORECASE
to ignore capitalization?
Unfortunately, the re.compile() function takes only a single value 
as its second argument.
You can get around this limitation by combining
the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables 
using the pipe character (|), which in this context is
known as the bitwise OR operator
'''
# for example:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
# or:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
