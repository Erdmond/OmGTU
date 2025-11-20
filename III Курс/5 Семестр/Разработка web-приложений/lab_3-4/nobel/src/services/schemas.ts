import * as t from 'io-ts';

const CountryCodec = t.partial({
  en: t.string
});

const PlaceCodec = t.partial({
  country: CountryCodec
});

const BirthCodec = t.partial({
  date: t.string,
  place: PlaceCodec
});

const NameCodec = t.partial({
  en: t.string
});

const MotivationCodec = t.partial({
  en: t.string
});

const CategoryCodec = t.partial({
  en: t.string
});

const NobelPrizeCodec = t.partial({
  awardYear: t.string,
  category: CategoryCodec,
  motivation: MotivationCodec
});

export const LaureateCodec = t.partial({
  id: t.string,
  fullName: NameCodec,
  birth: BirthCodec,
  nobelPrizes: t.array(NobelPrizeCodec)
});

export const NobelResponseCodec = t.partial({
  laureates: t.array(LaureateCodec),
  meta: t.partial({
    count: t.number
  })
});

export const PrizeCodec = t.partial({
  awardYear: t.string,
  category: CategoryCodec,
  dateAwarded: t.string,
  prizeAmount: t.number,
  prizeAmountAdjusted: t.number,
  laureates: t.array(t.partial({
    id: t.string,
    fullName: NameCodec,
        motivation: MotivationCodec,
  }))
});

export const PrizesResponseCodec = t.partial({
  nobelPrizes: t.array(PrizeCodec),
  meta: t.partial({
    count: t.number
  })
});

export type Prize = t.TypeOf<typeof PrizeCodec>;
export type PrizesResponse = t.TypeOf<typeof PrizesResponseCodec>;
export type Laureate = t.TypeOf<typeof LaureateCodec>;
export type NobelResponse = t.TypeOf<typeof NobelResponseCodec>;
export type NobelPrize = t.TypeOf<typeof NobelPrizeCodec>;
