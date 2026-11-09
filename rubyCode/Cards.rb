class Cards
  # Fields
  @@Deck = []
  @usr_hand = []
  @dealer_hand = []
  @balance = 0 # To be implemented

  # Constructor
  def initialize
    new_deck
  end

  #Methods

  def new_deck
    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    suits = ["S", "H", "C", "D"]
    ranks.each do |rank|
      suits.each do |suit|
        @@Deck.push([rank, suit])
      end
    end
  end

  def shuffle_deck
    @@Deck.shuffle!
  end

  def self.get_deck
    p @@Deck
  end
end