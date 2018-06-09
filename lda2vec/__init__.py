#<<<<<<< HEAD
#from .dirichlet_likelihood import dirichlet_likelihood
#from .embed_mixture import EmbedMixture
#from .tracking import Tracking
#from .preprocess import tokenize
#from .corpus import Corpus
#from .topics import prepare_topics, print_top_words_per_topic, topic_coherence
#from .negative_sampling import negative_sampling
#=======
from . import dirichlet_likelihood
from . import embed_mixture
from . import tracking
from . import preprocess
from . import corpus
from . import topics
from . import negative_sampling

dirichlet_likelihood = dirichlet_likelihood.dirichlet_likelihood
EmbedMixture = embed_mixture.EmbedMixture
Tracking = tracking.Tracking
tokenize = preprocess.tokenize
Corpus = corpus.Corpus
prepare_topics = topics.prepare_topics
print_top_words_per_topic = topics.print_top_words_per_topic
negative_sampling = negative_sampling.negative_sampling
topic_coherence = topics.topic_coherence

