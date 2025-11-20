import * as t from 'io-ts';
import { either } from 'fp-ts';
import { pipe } from 'fp-ts/function';

export function decodeOrThrow<T>(
  codec: t.Decoder<unknown, T>,
  data: unknown
): T {
  return pipe(
    codec.decode(data),
    either.fold(
      (errors) => {
        const errorMessages = errors.map(error => 
          `Path: ${error.context.map(ctx => ctx.key).join('.')}, ` +
          `Value: ${JSON.stringify(error.value)}, ` +
          `Message: ${error.message || 'Invalid value'}`
        ).join('\n');
        
        throw new Error(`Data validation failed:\n${errorMessages}`);
      },
      (decodedData) => decodedData
    )
  );
}

export function decodeSafe<T>(
  codec: t.Decoder<unknown, T>,
  data: unknown
): either.Either<t.Errors, T> {
  return codec.decode(data);
}
