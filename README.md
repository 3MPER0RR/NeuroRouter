## install 
git clone https://github.com/3MPER0RR/RamRouteAi/

cd RamRouteAi/project

touch .env

nano .env

insert in .env 

LLM_API_URL=https://api.groq.com/openai/v1/chat/completions

LLM_API_KEY=insert_apikey

LLM_MODEL=llama-3.3-70b-versatile

python3.11 -m venv venv

source venv/bin/activate

pip install -r requirements

# Requirements

- Python 3.11+

- Core dependencies:

numpy,httpx,python-dotenv

uvloop,orjson,scikit-learn,rich,psutil

RamRouteAI
A RAM-first routing layer for LLM APIs — reducing latency and API call volume through a complex-valued neural routing engine.

# The Problem
Every call to a remote LLM API introduces latency — typically between 300ms and 2 seconds per response — along with a per-token cost. In many real-world applications, a significant portion of incoming queries are semantically redundant: different phrasings of the same intent, repeated questions across sessions, or variations on a narrow domain of inputs. Each of these still pays the full cost of a remote round-trip.

# The Approach
RamRouteAI sits between your application and the LLM API. Incoming queries are embedded and compared against a semantic cache held entirely in RAM. If a query is sufficiently similar to a previously seen one — above a configurable similarity threshold — the cached response is returned locally, with sub-millisecond latency. Only genuinely novel queries are forwarded to the external API.

The routing decision is made by a complex-valued neural network (QNN) with phase-preserving activations, trained end-to-end via Wirtinger-calculus backpropagation and complex Adam optimization. Model weights are stored directly in a RAM-resident parameter server with nanosecond-level access latency and zero serialization overhead. Gradient correctness is verified against numerical finite-difference checks. The system supports Groq and any OpenAI-compatible endpoint as its external fallback.

# Performance
Benchmark results to be added. Target metrics: cache hit rate on representative workloads, mean latency with and without cache hit, RAM usage at varying cache sizes.

# Status
The disk-based execution layer is stable and considered production-ready. The RAM-based inference path is experimental and currently under active testing and validation.
Experimental prototype under active development.

Active development — modular components are being incrementally extended.
