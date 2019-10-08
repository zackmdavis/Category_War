### DRAFT: "Algorithms of Deception!"

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

For compatibility, we can imagine that Reporter and Audience are also written in Python. This is just for demonstration—the _real_ Reporter and Audience (out there in the world I'm asking you to imagine) might be much more complicated programs written for some kind of _alien_ computer the likes of which we have not yet dreamt!
But I like Python, and for the moment, we can pretend.

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

(If you noticed any similarity between the last two lines and the expression for [the mode of the Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution#Mode), that's _probably_ just a coincidence?)

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

It instead induces Audience to output a very different (and rather boring) distribution):

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

While the distribution that `reporter_2` makes Audience output isn't as boring as the one we saw for `reporter_1`, it still doesn't have the Very Interesting Property of matching the distribution of the $X_i$. Look at how much probability it assigns to the outcome "4":

[TODO: elaborate and explain that `reporter_2` at least _comes closer_ than reporter_1; the output still varies with reality; it's just distorted; whereas the liar was constant]

```
>>> audience(reporter_2([x() for _ in range(100000)]))
{1: 0.3971289947471831, 2: 0.20309555314968522, 3: 0.14860259032038173, 4: 0.2516540358474678}
```

So far, all of the Reporters we've imagined 


-----

**Author's commentary (for email pre-readers, not for publication)**:

I'm interested in solving this recurring inferential distance problem—

Blight-alarmists say, "Fraud!"

Blight-denialists say, "How dare you?! Sure, maybe people sometimes say things that are false due to self-interested bias—that's a great motte. But this tendentious rhetoric of calling it _fraud_—you can't have that bailey."

Blight-alarmists say, "What the fuck do you think 'fraud' is, if it's not systematically saying things that aren't true in a direction that moves resources towards you?! I'm not convinced you're trying to create clarity here; if you're going to troll me like this, then I refuse to do any more interpretive labor."

Blight-denialists say, "!?!"

Alarmists claim that they/we want to model political distortions on our collective epistemology. Denialists think that alarmists are just doing their own brand of coalitional politics by using inherently morally-charged language and falsely claiming that no moral connotations are intended.

I'm interested in _complying_ with the demand for non-morally-charged language as much as I possibly can. (["Bad intent is a disposition, not a feeling"](http://benjaminrosshoffman.com/bad-faith-behavior-not-feeling/) was a great start, but doesn't go as far in this direction as I'm trying to go.) _Start_ with toy code/math models about programs that output data that make other programs make worse predictions, and _then_ slowly build up to, "We don't care about your conscious verbal narrative! Your narrative is _bullshit_! We care about systematic deviations from ideal map–territory entanglement!"
