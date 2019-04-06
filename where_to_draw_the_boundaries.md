"Where to Draw the Boundaries?"

**Followup to:** [Where to Draw the Boundary?](https://www.lesswrong.com/posts/d5NyJ2Lf6N22AD9PB/where-to-draw-the-boundary)

_Figuring where to cut reality in order to carve along the joints—figuring which things are similar to each other, which things are clustered together:_ this _is the problem worthy of a rationalist. It is what people_ should _be trying to do, when they set out in search of the floating essence of a word._

_Once upon a time it was thought that the word "fish" included dolphins ..._

The one comes to you and says:

> The list: `{salmon, guppies, sharks, dolphins, trout}` is just a list—you can't say that a list is _wrong_. You draw category boundaries in specific ways to capture tradeoffs you care about: sailors in the ancient world wanted a word to describe the swimming finned creatures that they saw in the sea, which included salmon, guppies, sharks—and dolphins. That grouping may not be the one favored by modern biologists, but an alternative categorization system is not an error, and borders are not objectively true or false. You're not standing in defense of truth if you insist on a word, brought explicitly into question, being used with some particular meaning. So my definition of _fish_ cannot possibly be 'wrong,' as you claim. I can define a word any way I want—in accordance with my values!

So, there is a legitimate complaint here. It's true that sailors in the ancient world had a legitimate reason to want a word in their language whose [extension](https://www.lesswrong.com/posts/HsznWM9A7NiuGsp28/extensions-and-intensions) was `{salmon, guppies, sharks, dolphins, ...}`. (And modern scholars writing a translation for present-day English speakers might even be tempted to translate that word as _fish_, because most members of that category are what we would call fish.) It indeed would not necessarily be helping the sailors to tell them that they need to exclude dolphins from the extension of that word, and instead include dolphins in the extension of their word for `{monkeys, squirrels, horses ...}`. Likewise, modern biologists have no need for a word that groups dolphins and guppies together.

When rationalists say that definitions can be wrong, we don't mean that there's a _unique_ category boundary that is the True floating essence of a word, and that all other possible boundaries are wrong.

[...]

The one replies—

> But reality doesn't come with its joints pre-labeled. Questions about how to draw category boundaries are best understood as questions about values or priorities rather than about the actual content of the actual world. Everything we identify as a joint is only a joint because we care about it.



Everything we identify as a joint is a joint not "because we care about it", but because it _helps us think about_ the things we care about.

There is an _important difference_ between "not including mountains on a map because it's a political map that doesn't show any mountains" and "not including Mt. Everest on a geographic map, because my friends don't like Mt. Everest and would be upset if they saw it on my map."

There is an _important difference_ between "identifying this pill as not being 'poison' allows me to concentrate my probability-mass when [anticipating](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences) what I'll observe after administering the pill to a human (even if [most possible minds](https://www.lesswrong.com/posts/tnWRXkcDi5Tw9rzXw/the-design-space-of-minds-in-general) have never seen a 'human' and would never waste cycles imagining administering the pill to one)" and "identifying this pill as not being 'poison', because if I did call it 'poison', then the manufacturer of the pill might sue me."

There is an _important difference_ between having a utility function defined over a statistical model's _performance_ against specific real-world data (even if another mind with different values would be interested in different data), and having a utility function defined over features of _the model itself_.



You _can't_ change the categories your mind _actually_ uses and still perform as well on prediction tasks, although you can change your [_verbally reported_](https://www.lesswrong.com/posts/NMoLJuDJEms7Ku9XS/guessing-the-teacher-s-password) categories, much as how one can verbally report "believing" in an [invisible, inaudiable, flour-permeable dragon](https://www.lesswrong.com/posts/CqyJzDZWvGhhFJ7dY/belief-in-belief) in one's garage without having any false anticipations-of-experience about the garage.

This may be easier to see with a simple _numerical_ example.

Suppose we have some entities that exist in the three-dimensional vector space ℝ³. There's one cluster of entities centered at [1, 2, 3], and we call those entities Foos, and there's another cluster of entities centered at [2, 4, 6], which we call Quuxes.

The one comes and says, "Well, I'm going redefine the meaning of 'Foo' such that it also includes the things near [2, 4, 6] as well as the Foos-with-respect-to-the-old-definition, and you can't say my new definition is wrong, because if I observe [2, \_, \_] (where the underscores represent yet-unobserved variables), I'm going to categorize that entity as a Foo but still predict that the unobserved variables are 4 and 6, _so there_."

But if the one were _actually using_ the new definition of Foo _internally_ and not just _saying the words_ "categorize it as a Foo", they _wouldn't_ predict 4 and 6! They'd predict 3 and 4.5, because those are the average values of a generic Foo-with-respect-to-the-new-definition in the 2nd and 3rd coordinates (because (2+4)/2 = 6/2 = 3 and (3+6)/2 = 9/2 = 4.5). (The already-observed 2 in the first coordinate isn't average, but by [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes), that only affects our prediction of the other two variables _by means_ of its effect on our "prediction" of category-membership.) The cluster-structure knowledge that "entities for which x₁≈2, also tend to have x₂≈4 and x₃≈6" needs to be represented _somewhere_ in the one's mind _in order to get the right answer_. And given that that knowledge needs to be represented, it might also be useful to have a _word_ for "the things near [2, 4, 6]" in order to efficiently share that knowledge with others.

Certainly, there isn't going to be a _unique_ way to encode the knowledge into natural language: there's no rule of rationality that says the word/symbol "Foo" needs to represent "the stuff near [1, 2, 3]" rather than "both the stuff near [1, 2, 3] and also the stuff near [2, 4, 6]". But if speakers of particular language were _already_ using "Foo" to specifically talk about the stuff near [1, 2, 3], then you can't swap in a new definition of "Foo" without _changing the truth values_ of sentences involving the word "Foo." Or rather: sentences involving Foo-with-respect-to-the-old-definition [are _different_ propositions](https://www.lesswrong.com/posts/shoMpaoZypfkXv84Y/variable-question-fallacies) from sentences involving Foo-with-respect-to-the-new-definition, even if they get written down using the same symbols in the same order.

Certainly, this all becomes much more complicated as we move away from the simplest idealized examples. For example, if the points are more evenly distributed in configuration space rather than belonging to cleanly distinguishable clusters, then essentialist "X is a Y" cognitive algorithms perform less well, and we get [Sorities paradox](https://plato.stanford.edu/entries/sorites-paradox/) situations where the mapping of structure-in-the-world to human natural language is a lot messier. Or, as with the fish _vs._ _dagim_ example, it might not be clear which aspects of reality are most relevant. (Clusters can "split" or "collapse" depending on _which_ dimensions of configuration space you want to look at.) Or there might be social or psychological forces anchoring word usages on easily-distinguishable Schelling points, even at the cost of some statistical "fit."

We could go on listing more such complications. But the fundamental thing is this: _the map is not the territory_. Maybe sometimes we might _want_ something to belong to a category that it currently doesn't.


Miyamoto Musashi [is quoted as saying](http://yudkowsky.net/rational/virtues/):

> The primary thing when you take a sword in your hands is your intention to cut the enemy, whatever the means. Whenever you parry, hit, spring, strike or touch the enemy's cutting sword, you must cut the enemy in the same movement. It is essential to attain this. If you think only of hitting, springing, striking or touching the enemy, you will not be able actually to cut him.

Similarly, the primary thing when you take a word in your lips is your intention to reflect the territory, whatever the means. Whenever you categorize, label, name, define, or draw boundaries, you must _cut through to the correct answer in the same movement_. If you think only of categorizing, labeling, naming, defining, or drawing boundaries, you will not be able to actually reflect the territory.

Do not ask whether there's a rule of rationality saying that you shouldn't call dolphins fish. Ask whether dolphins are fish.

And if you speak overmuch of the Way you will not attain it.
