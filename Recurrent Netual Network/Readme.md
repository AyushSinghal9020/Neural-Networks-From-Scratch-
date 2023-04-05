# Recurrent Neural Network

Recurrent Neural Networks (RNN) are a type of neural network that can process sequences of data, such as time-series data or natural language. Unlike feedforward neural networks, which only process one input at a time and have no memory, RNNs can maintain information about previous inputs and use it to inform the processing of future inputs.

RNNs are made up of a series of interconnected nodes or "cells," which have a loop that allows them to maintain a "state" or memory. Each cell takes as input the current input and the previous state, and produces an output and an updated state. The output can be used for prediction or classification tasks, while the updated state is passed on to the next cell in the sequence.

One of the key advantages of RNNs is their ability to process variable-length sequences. This makes them well-suited for tasks such as speech recognition, machine translation, and sentiment analysis, where the length of the input can vary greatly. However, RNNs can suffer from the "vanishing gradient" problem, which can make it difficult for the network to learn long-term dependencies in the input sequence.

To address this issue, various modifications to the basic RNN architecture have been proposed, such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) cells. These variants use gating mechanisms to control the flow of information within the network, allowing it to more effectively learn long-term dependencies.

Overall, RNNs are a powerful tool for processing sequential data, and have found widespread use in a variety of fields, including natural language processing, speech recognition, and music generation.

****

**Note** - This notebook is highly inspired by this [Youtube Video](https://www.youtube.com/watch?v=4wuIOcD1LLI)


**KUDOS TO THE TEACHER**

