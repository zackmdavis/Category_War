### "Algorithms of Deception!"

I want you to imagine a world consisting of a sequence of independent and identically distributed random variables $X_i$, and two computer programs.

The first program is called Reporter. As input, it accepts a bunch of the random variables $X_i$. As output, it returns a list of lists whose elements belong to the domain of the $X_i$.

The second program is called Audience. As input, it accepts the output of Reporter. As output, it returns a probability distribution.

Suppose the $X_i$ exhibit the following distribution:

$$P_A(X_i) = \begin{cases} 1/2 & X_i = 1 \\ 1/4 & X_i = 2 \\ 3/16 & X_i = 3 \\ 1/16 & X_i = 4 \\ \end{cases}$$

We can model drawing a sample from this distribution using this function in the Python programming language:

```
import random

def x():
    r = random.random()
    if 0 <= r < 1/2:
        return 1
    elif 1/2 <= r < 3/4:
        return 2
    elif 3/4 <= r < 15/16:
        return 3
    else:
        return 4
```

For compatibility, we can imagine that Reporter and Audience are also written in Python. This is just for demonstration in the blog post that I'm writing—the _real_ Reporter and Audience (out there in the world I'm asking you to imagine) might be much more complicated programs written for some kind of _alien_ computer the likes of which we have not yet dreamt! But I like Python, and for the moment, we can pretend.

So pretend that Audience looks like this (where the dictionary represents a probability distribution, with the keys being random-variable outcomes and the values being probabilities):

```
from collections import Counter

def audience(report):
    a = Counter()
    for sight in report:
        for possibility in sight:
            a[possibility] += 1/len(sight)            
    d = sum(a_j - len(a) for a_j in a.values())
    return {x: (a_i - 1)/d for x, a_i in a.items()}
```

(If you noticed any similarity between the last two lines and the expression for [the mode of the Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution#Mode), that's _probably_ just a coincidence?)[^wrong]

[^wrong]: And, um, this is actually wrong. 

Let's consider multiple possibilities for the form that Reporter could take. A particularly simple implementation of Reporter (call it `reporter_0`) might look like this:

```
def reporter_0(xs):
    output = []
    for x in xs:
        output.append([x])
    return output
```

This version of Reporter has a _Very Interesting Property!_ When we call Audience on the output of this Reporter, the probability distribution that Audience returns is _very similar_ to the distribution that our random variable is from!

```
>>> audience(reporter_0([x() for _ in range(100000)]))
{1: 0.5003300528084493, 2: 0.2502900464074252, 3: 0.1873799807969275, 4: 0.062119939190270444}

# Compare to the distribution of X_i expressed as a Python dictionary—
>>> {1: 1/2, 2: 1/4, 3: 3/16, 4: 1/16}
{1: 0.5, 2: 0.25, 3: 0.1875, 4: 0.0625}
```

Weird, right?!

Of course, there are _other_ possible implementations of Reporter. For example, this Reporter (`reporter_1`) does _not_ have the Very Interesting Property—

```
def reporter_1(xs):
    output = []
    for _ in range(len(xs)):
        output.append([4])
    return output
```

It instead induces Audience to output a very different (and rather boring) distribution). It doesn't even matter how the $X_i$ turned up; the result will always be the same:

```
>>> audience(reporter_1([x() for _ in range(100000)]))
{4: 1.0}
```

We could go on imagining other versions of Reporter, like this one (`reporter_2`)—

```
def reporter_2(xs):
    output = []
    for x in xs:
        if x == 4 or random.random() < 0.2:
            output.append([x])
        else:
            continue
    return output
```

While the distribution that `reporter_2` makes Audience output isn't as boring as the one we saw for `reporter_1`, it still doesn't have the Very Interesting Property of matching the distribution of the $X_i$. It comes _closer_ to having the Very Interesting Property than `reporter_1` did—notice how the _ratios_ of probabilities assigned to the first three outcomes is similar to that of the original distribution, but it's assigning way too much probability-mass to the outcome "4"—

```
>>> audience(reporter_2([x() for _ in range(100000)]))
{1: 0.3971289947471831, 2: 0.20309555314968522, 3: 0.14860259032038173, 4: 0.2516540358474678}
```

So far, all of the Reporters we've imagined are still only putting one element in the inner lists of the list-of-lists that they return. But we could imagine `reporter_3`—

```
def reporter_3(xs):
    output = []
    for x in xs:
        if x in [1, 4]:
            output.append([1, 4])
        else:
            output.append([x])
    return output
```

Unlike `reporter_2` (which typically returned a list with _fewer_ elements than it received as input), the list returned by `reporter_3` has exactly as many elements as the list it took in. Yet this Reporter still prompts Audience to return a distribution with too many "4"s—and _unlike_ `reporter_2`, it doesn't even get the ratio of the other outcomes right, yielding disproportionately fewer "1"s _vs._ "2"s and "3"s compared to the original distribution—

```
>>> audience(reporter_3([x() for _ in range(100000)]))
{1: 0.2808949431909106, 2: 0.24795967354776766, 3: 0.19037045927348376, 4: 0.2808949431909106}
```

Again, I've presented Audience and the various Reporters as simple Python programs for illustration and simplicity, but the same _input-output relationships_ could be embodied by more complicated systems—perhaps an entire conscious mind which could talk.

After the inferred frequency of "4"s failed to appear, perhaps Audience would say, "I _trusted_ you, and you _lied_ to me!"

And `reporter_2` might defend itself: "How dare you accuse me of _lying_!? Sure, I'm not a perfect program free from all bias, but every outcome I reported corresponded to one of the $X_i$—I never told a mistruth."

And `reporter_3` might defend itself: "I can define a word any way I want! Unlike `reporter_2`, I'm not being selective—everything I saw, I reported.

[TODO: explain the problem where grouping the rare "4" and the common "1" into the same category artificially makes the former seem more common, if the listener cares about the difference and doesn't know the priors—probably give this line to "Audience"]

[TODO: wrap up the moral: outright-lying, selective-reporting, and category-gerrymandering are all examples of _algorithms of deception_: ways of communicating that cause listeners to make bad predictions (compared to the listener running the same inference algorithm on honest reports). It's kind of dysfunctional to care too much about lying vs. not-lying, or conscious-lying vs. unconscious-rationaliation, when the _outcomes_ are the same. (_Incentives_ matter—there's a reason vehicular manslaughter is punished differently from first-degree murder—but either way, the person is _still equally dead_.)]
